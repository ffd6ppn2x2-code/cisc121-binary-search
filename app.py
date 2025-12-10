import gradio as gr
from gradio.themes import Soft

def parse_list(list_str):
    """
    Turn a comma-separated string into a list of integers.
    Example: "1, 3, 5" -> [1, 3, 5]
    """
    parts = [x.strip() for x in list_str.split(",") if x.strip() != ""]
    try:
        nums = [int(x) for x in parts]
    except ValueError:
        raise ValueError("Please enter only whole numbers separated by commas.")
    return nums


def binary_search_with_steps(arr, target):
    """
    Binary search that also returns a text log of what happened.
    """
    steps = []
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        value = arr[mid]

        steps.append(f"low={low}, high={high}, mid={mid}, value={value}")

        if value == target:
            steps.append(f"✅ Found {target} at index {mid}.")
            return mid, "\n\n".join(steps)
        elif value > target:
            steps.append(f"{value} is bigger than {target}, go LEFT (high = mid - 1).")
            high = mid - 1
        else:
            steps.append(f"{value} is smaller than {target}, go RIGHT (low = mid + 1).")
            low = mid + 1

    steps.append(f"❌ {target} is not in the list.")
    return -1, "\n\n".join(steps)


def run_binary_search(list_str, target):
    """
    Wrapper that:
    - parses the list string,
    - makes sure it's sorted,
    - calls binary search,
    - formats a nice result for the UI.
    """
    nums = parse_list(list_str)

    sorted_info = ""
    if nums != sorted(nums):
        nums = sorted(nums)
        sorted_info = "Note: your list was not sorted, so I sorted it first.\n\n"

    index, steps = binary_search_with_steps(nums, target)

    result_text = f"Sorted list: {nums}\n\n"
    if index == -1:
        result_text += f"Result: {target} was NOT found.\n\n"
    else:
        result_text += f"Result: {target} was found at index {index}.\n\n"

    result_text += sorted_info + "Steps:\n\n" + steps
    return result_text


with gr.Blocks(theme=Soft()) as demo:
    gr.Markdown(
        """
        <div style="text-align:center; padding: 12px 0;">
            <div style="font-size: 34px; font-weight: 800; letter-spacing: -0.4px;">
                Binary Search Visualizer
            </div>
            <div style="font-size: 16px; color: #4b5563;">
                Paste a list, pick a target, and see each decision in the search.
            </div>
        </div>
        """
    )

    with gr.Row():
        with gr.Column(scale=3):
            input_list = gr.Textbox(
                label="List (comma-separated integers)",
                placeholder="Example: 1, 3, 5, 7, 9",
                lines=3,
            )
            target_number = gr.Number(
                label="Target to search for",
                precision=0,
            )
            gr.Examples(
                examples=[
                    ["1, 3, 5, 7, 9", 7],
                    ["2, 4, 6, 8, 10, 12", 5],
                    ["5, 5, 5, 5", 5],
                    ["-10, -4, 0, 3, 6, 12", -4],
                ],
                inputs=[input_list, target_number],
                label="Quick examples",
            )
        with gr.Column(scale=4):
            result_box = gr.Textbox(
                label="Result + Steps (spaced for readability)",
                lines=18,
            )

    gr.Markdown(
        """
        <div style="font-size: 14px; color: #4b5563; padding: 6px 4px;">
            • Lists are auto-sorted if needed.<br>
            • Steps are spaced out so you can skim how low/mid/high move.<br>
            • Works best with small-to-medium lists to see the decisions clearly.
        </div>
        """
    )

    run_button = gr.Button("Run Binary Search", variant="primary")
    run_button.click(run_binary_search, inputs=[input_list, target_number], outputs=result_box)


if __name__ == "__main__":
    demo.launch(theme=Soft())
