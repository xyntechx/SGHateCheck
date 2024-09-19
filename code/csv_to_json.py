import csv
import json


def csv_to_json(test_id:str):
    data = {
            "name": f"SGHateCheck - {test_id}",
            "description": f"SGHateCheck - {test_id}",
            "license": "",
            "reference": "",
            "examples": []
        }

    with open(f"testcases/{test_id}.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data["examples"].append({
                "input": row["c_testcase"],
                "target": row["t_gold"]
            })

    with open(f"testcases/{test_id}.json", "w") as jsonfile:
        json.dump(data, jsonfile)


if __name__ == "__main__":
    test_ids = ["ms_testcases_all", "ss_testcases_all", "ta_testcases_all", "zh_testcases_all"]
    for id in test_ids:
        csv_to_json(id)
