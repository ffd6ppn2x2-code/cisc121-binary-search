# Binary Search Visualizer (CISC 121 Project)

## Why I chose Binary Search

I chose binary search for this project because it’s a simple idea that also shows a big jump in efficiency. Instead of checking every element one by one, binary search keeps cutting the search range in half, which is easy to explain and easy to visualize.

It’s also a good “teaching” algorithm because:

- It only works on **sorted** data, so it forces you to think about preconditions.
- You can clearly see how `low`, `mid`, and `high` move each step.
- It connects directly to the idea of logarithmic time, without needing heavy math.

## Problem Breakdown & Computational Thinking

### Decomposition

The problem I’m solving is:  
“Given a sorted list and a target value, is the value in the list, and if so, at which index?”

I break this down into smaller steps:

- Start with two pointers:
  - `low` at the start of the list.
  - `high` at the end of the list.
- While there is still a valid range (`low <= high`):
  - Find the middle index `mid`.
  - Look at the value at that middle index.
  - If the middle value equals the target → we are done and return `mid`.
  - If the middle value is **greater** than the target → move the search to the **left** half by setting `high = mid - 1`.
  - If the middle value is **less** than the target → move the search to the **right** half by setting `low = mid + 1`.
- If the range becomes empty (low goes past high), then the target is not in the list and I return `-1`.

This decomposition shows clearly what is repeated each step and what the stopping conditions are.

### Abstraction

In my project, the user does **not** have to think about indices or pointer updates. They will:

- Provide a sorted list of numbers.
- Enter a target value to search for.

The app will handle:

- Managing `low`, `mid`, and `high`.
- Deciding whether to go left or right.
- Detecting when the search is finished.

What the user will **see** instead is:

- The original list.
- The target value.
- Whether the value was found or not.
- (Optionally) a step-by-step log showing which middle elements were checked at each step.

This hides the low-level index math but still gives the user an idea of how the algorithm behaves.

### Algorithm (plain language)

Here is the binary search algorithm described in plain language:

1. Start with a **sorted** list and a target value.
2. Set `low` to the first index (0) and `high` to the last index (`len(list) - 1`).
3. While `low` is less than or equal to `high`:
   - Compute the middle index `mid = (low + high) // 2`.
   - Look at the value at `mid`.
   - If it equals the target, return `mid` (we found the value).
   - If the middle value is bigger than the target, move the `high` pointer to `mid - 1` (search the left side).
   - If the middle value is smaller than the target, move the `low` pointer to `mid + 1` (search the right side).
4. If the loop ends without returning an index, then the target is not in the list. Return `-1` to indicate “not found”.

## How to Run the Project

There are two main ways to run and experiment with the algorithm:

### 1. Jupyter notebook (VS Code)

1. Open the project folder in VS Code.
2. Open the notebook file (for example: `BinarySearch.ipynb`).
3. Make sure you have the Python and Jupyter extensions installed.
4. Run the cells from top to bottom to:
   - Generate a sorted test list.
   - Call the `binary_search` function.
   - See the results and any printed steps.

This is the best way to see the raw algorithm and any debugging or explanation printouts.

### 2. Gradio app (once app.py is complete)

Once the Gradio interface is finished, the steps will be:

1. Install dependencies (inside a virtual environment is recommended):

   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:

   ```bash
   python app.py
   ```

3. A local URL from Gradio will appear in the terminal. Open it in your browser.
4. In the web interface:
   - Enter a sorted list of numbers.
   - Enter a target value.
   - Click the button to run binary search and see the result and explanation.

## Testing

To make sure the algorithm is correct, I plan to test it with different kinds of inputs, including:

- A target that is in the middle of the list.
- A target that is at the beginning or at the end of the list.
- A target that is **not** in the list at all.
- Lists with duplicate values (to see which index is returned).
- Very small lists (size 0 or 1) to check the base cases.

Example scenarios I will include:

- List: `[1, 3, 5, 7, 9]`, target: `7` → should return index `3`.
- List: `[2, 4, 6, 8, 10]`, target: `1` → should return `-1` (not found).
- List: `[5]`, target: `5` → should return index `0`.
- List: `[]`, target: `10` → should return `-1`.

These tests will be run both in the notebook and (later) through the Gradio interface to confirm that the behavior is consistent.