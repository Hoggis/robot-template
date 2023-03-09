"""
Python endpoint for starting the robot.
"""
import argparse
import os
import sys
from glob import glob

import robot

from resources.settings import PACKAGE_ROOT

if not sys.version_info[0] == 3:
    sys.exit("Please run this with Python 3.")

# Populate this tuple with your desired stages
VALID_STAGES = (0, 1)


def write_errors_file(output_dir):
    """Collect all errors from robot output files and writes them to `errors.txt`.
    The file contents can be used programmatically in automatic alerts etc."""
    result = robot.api.ExecutionResult(glob(f"{output_dir}/*.xml")[0])
    errors = list(filter(lambda err: err.level == "ERROR", result.errors))
    timestamps = [err.timestamp for err in errors]

    with open(os.path.join(output_dir, "errors.txt"), "w") as errors_file:
        for time, err in zip(timestamps, errors):
            errors_file.write(f"{time}: {err}\n\n")


def main():
    args = parse_args()
    output_dir = os.path.join(PACKAGE_ROOT, "output")

    status = robot.run(
        os.path.join(PACKAGE_ROOT, "tasks", "main.robot"),
        include=args.stages,
        variable=[
            f"env:{args.env}",
        ],
        exitonfailure=True,
        exitonerror=True,
        dryrun=args.dryrun,
        runemptysuite=True,
        timestampoutputs=True,
        outputdir=output_dir,
    )

    try:
        # this feature is experimental
        write_errors_file(output_dir)
    finally:
        return sys.exit(status)


def parse_args():
    def robot_stage(stage):
        """Prefix stage argument with `stage_` if it is int."""
        try:
            return f"stage_{int(stage)}"
        except ValueError:
            return stage

    parser = argparse.ArgumentParser(
        description="Main entrypoint",
        usage="python run.py 0 1",
    )
    # fmt: off
    parser.add_argument(
        "stages",
        nargs="*",
        type=robot_stage,
        choices=[f"stage_{i}" for i in VALID_STAGES],
        help=f"Give the stages you wish to run {VALID_STAGES}"
    )
    parser.add_argument(
        "-e",
        "--env",
        default="dev",
        help="Environment: [dev|test|prod]"
    )
    parser.add_argument(
        "--dryrun",
        action="store_true",
        help="Only do Robot Framework dry run"
    )
    # fmt: on

    return parser.parse_args()


def parse_stages(args):
    stages = args.stages

    for stage in stages:
        if stage not in VALID_STAGES:
            print("Please give a valid stage number:", VALID_STAGES)
            sys.exit(1)

    return [f"stage_{stage}" for stage in stages]


if __name__ == "__main__":
    main()
