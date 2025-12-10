import argparse
import json
import os


def config() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run judge on the benchmark"
    )

    # environment config
    parser.add_argument(
        "--result_dir",
        type=str,
        default="results/pyautogui/screenshot"
    )
    parser.add_argument(
        "--model", type=str, default="qwen2.5:3b"
    )
    parser.add_argument(
        "--domain", type=str, default="multi_apps"
    )
    args = parser.parse_args()

    return args

if __name__ == "__main__":
    args = config()

    # save args to json in result_dir/action_space/observation_type/model/args.json
    results_dir = os.path.join(
        args.result_dir,
        args.model.split(':')[-0]+'-'+args.model.split(':')[-1],
        args.domain
    )

    success_rate = 0
    WES_minus = 0
    WES_plus = 0
    case_cnt = 0

    for case in os.listdir(results_dir):
        case_path = os.path.join(results_dir, case)
        if not os.path.isdir(case_path):
            continue

        case_cnt += 1

        step_cnt = sum(
            1 for file in os.listdir(case_path)
            if file.lower().endswith(".png")
        )
        if step_cnt > 0:
            step_cnt -= 1

        float_value = None
        results_file = os.path.join(case_path, 'result.txt')
        if not os.path.exists(results_file):
            continue

        try:
            with open(results_file, "r") as f:
                value_str = f.read().split("\n")[0]
                value = float(value_str)
                success_rate += value
                if value == 0:
                    WES_minus -= step_cnt
                else:
                    WES_plus += step_cnt
        except Exception as e:
            print(f"Failed to read float from {results_file}: {e}")
            continue

        if float_value is None:
            float_value = 0.0

    WES_minus /= case_cnt
    WES_plus /= case_cnt

    print(f"Success rate: {success_rate}\n", f"WES+: {WES_plus}\n", f"WES+: {WES_minus}")

