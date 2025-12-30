import json

FILE_NAME = "items.json"

items = []


def calculate_score(need, want):
    return need * (1 - want / 100)


def get_label(need, want):
    if need >= 70 and want <= 30:
        return "Essential"
    elif want > need:
        return "Emotional"
    elif want >= 70 and need <= 30:
        return "Neglect"
    else:
        return "Justified"


def save_items():
    with open(FILE_NAME, "w") as file:
        json.dump(items, file, indent=4)


def load_items():
    global items
    try:
        with open(FILE_NAME, "r") as file:
            items = json.load(file)
    except FileNotFoundError:
        items = []


def add_item():
    name = input("Item name: ")

    need = int(input("Need percentage (0-100): "))
    want = int(input("Want percentage (0-100): "))

    score = calculate_score(need, want)

    item = {"name": name, "need": need, "want": want, "score": score}

    items.append(item)
    save_items()

    print("Item added successfully!\n")


def list_items():
    if not items:
        print("No items yet.\n")
        return

    sorted_items = sorted(items, key=lambda x: x["score"], reverse=True)

    print("\n--- Items ---")
    for item in sorted_items:
        label = get_label(item["need"], item["want"])
        print(
            f"{item['name']} | "
            f"Need: {item['need']}% | "
            f"Want: {item['want']}% | "
            f"Score: {item['score']:.2f} | "
            f"{label}"
        )
    print()


def main():
    while True:
        print("1. Add item")
        print("2. List Items")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            list_items()
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("Invalid choice\n")


main()
