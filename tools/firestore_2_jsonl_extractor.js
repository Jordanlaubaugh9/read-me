const admin = require("firebase-admin");
const fs = require("fs");

// Initialize Firebase Admin
const serviceAccount = require("./firebase-service.json");
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
});
const db = admin.firestore();

async function fetchDocuments(lastDocId = null) {
  let query = db.collection("collection_name").limit(500);

  if (lastDocId) {
    try {
      const lastDoc = await db
        .collection("collection_name")
        .doc(lastDocId)
        .get();
      if (lastDoc.exists) {
        query = query.startAfter(lastDoc);
      } else {
        console.log(`Last document with ID ${lastDocId} does not exist.`);
      }
    } catch (error) {
      console.error(`Error retrieving last document: ${error}`);
      return [];
    }
  }

  try {
    const snapshot = await query.get();
    return snapshot.docs;
  } catch (error) {
    console.error(`Error fetching documents: ${error}`);
    return [];
  }
}

function saveToJson(writeStream, docs) {
  for (const doc of docs) {
    const data = { id: doc.id, ...doc.data() };
    writeStream.write(JSON.stringify(data) + "\n");
  }
}

async function copyAndDeleteDocuments(docs, collectionName) {
  const batch = db.batch();
  docs.forEach((doc) => {
    const newDocRef = db.collection(collectionName).doc(doc.id);
    const originalDocRef = db.collection("original_collection").doc(doc.id);
    batch.set(newDocRef, doc.data());
    batch.delete(originalDocRef);
  });

  try {
    await batch.commit();
  } catch (error) {
    console.error("Failed to commit batch:", error);
    throw new Error("Batch commit failed"); // Rethrowing the error will stop the process if critical
  }
}

async function processDocuments() {
  let lastDocId = null;
  try {
    lastDocId = fs.readFileSync("lastDocId.txt", "utf8");
  } catch (err) {
    console.log("Starting from the beginning...");
  }

  const writeStream = fs.createWriteStream("output.jsonl", { flags: "a" });

  while (true) {
    const docs = await fetchDocuments(lastDocId);
    if (docs.length === 0) {
      console.log("No more documents to process");
      break;
    }

    saveToJson(writeStream, docs);
    try {
      await copyAndDeleteDocuments(docs, "proccessed_collection_name"); // Copy the processed docs to a new collection so this program can be run multiple times on large collections.
      lastDocId = docs[docs.length - 1].id;
      fs.writeFileSync("lastDocId.txt", lastDocId);
    } catch (error) {
      console.error("Error during document processing:", error);
      break; // Exit or handle retry logic
    }
  }
  writeStream.end();
}

processDocuments().catch(console.error);
