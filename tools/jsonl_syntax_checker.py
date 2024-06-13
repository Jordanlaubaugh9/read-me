import ijson


def check_jsonl_syntax(file_path):
    error_count = 0
    item_count = 0

    with open(file_path, "r") as file:
        for line in file:
            try:
                ijson.parse(line)
                item_count += 1
            except ijson.JSONError as err:
                error_count += 1
                print(f"Syntax error at item {item_count + 1}: {err}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

    print(
        f"Finished checking JSON. Total items parsed: {item_count}, errors found: {error_count}"
    )


check_jsonl_syntax("file_path.jsonl")
