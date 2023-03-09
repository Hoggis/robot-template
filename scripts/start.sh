# !/bin/bash

# A collection of bash functions to help running different stages. Modify according to your needs.

export ROBOT_ENV="${ROBOT_ENV:=dev}"
export ROBOT_STAGES="${ROBOT_STAGES:=0}"
export CHROME_VERSION="${CHROME_VERSION:=latest}"
export WORKSPACE="${WORKSPACE:=$(pwd)}"

setup_env() {
    echo "Setting up Python venv..."
    python3 -m venv ./.venv
    . ./.venv/bin/activate
    pip install -r ./requirements.txt
    echo "Venv setup complete, python resolves to: $(which python)"
    python --version
    webdrivermanager -l $WORKSPACE chrome:$CHROME_VERSION
}

# If a display is needed:
setup_xvfb() {
    export DISPLAY=:89

    # Start Xvfb, a virtual X server
    xvfb_running=`ps aux | grep "Xvfb :89" | grep -v grep`
    if [ -e /tmp/.X89-lock ]; then
        echo "Xvfb server already running on screen :89"
    else
        echo "Starting Xvfb server"
        Xvfb $DISPLAY -screen 0 1024x768x16 -ac &
    fi

    # Start fluxbox, a minimal window manager for X
    if pgrep -x fluxbox > /dev/null; then
        echo "Fluxbox already running"
    else
        echo "Starting Fluxbox"
        fluxbox >> fluxbox.log 2>&1 &
    fi
}

test() {
    echo "Running robot tests..."
    . ./.venv/bin/activate
    pip install -r ./requirements-test.txt
    pytest --pylint || exit $?
    rflint -A .rflintargs tasks || exit $?
    python run.py --env test $ROBOT_STAGES --dryrun
}

safety() {
    echo "Running safety..."
    . ./.venv/bin/activate
    pip install safety
    python -m safety check --full-report
}

process() {
    echo "Running robot process..."
    . ./.venv/bin/activate
    python run.py --env $ROBOT_ENV $ROBOT_STAGES
}

merge_logs() {
    . ./.venv/bin/activate
    rebot --merge -o output.xml --outputdir output output/output*.xml
}

"$@" || exit $?