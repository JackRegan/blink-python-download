# Blink Clip Downloader

This script downloads all available video clips from your Blink security cameras using the [blinkpy](https://github.com/fronzbot/blinkpy) Python library.

## Features

- Authenticates with your Blink account.
- Automatically finds all cameras on your account.
- Downloads all available video clips since the beginning of your account history.
- Saves clips to a local directory (`blink_clips` by default).

## Requirements

- Python 3.7+
- [blinkpy](https://github.com/fronzbot/blinkpy)
- [aiohttp](https://docs.aiohttp.org/en/stable/)
- An active Blink account (email and password)

## Setup

1. **Clone or copy this script to your project directory.**
2. **Create and activate a Python virtual environment (optional but recommended):**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
3. **Install dependencies:**
    ```bash
    pip install blinkpy aiohttp
    ```

## Usage

1. **Run the script:**
    ```bash
    python download_blink_clips_v2.py
    ```
2. **Enter your Blink account password when prompted.**
3. **If prompted for a verification code, check your email and enter the code.**
4. **Clips will be downloaded to the `blink_clips` directory.**

## Notes

- The script uses your Blink email address as configured in the `EMAIL` variable. Change this in the script if needed.
- All available clips since the start of your account will be downloaded. You can adjust the `since` parameter in the script to limit the date range.
- If you encounter issues, ensure your credentials are correct and that your Blink account has active cameras with available clips.

## Disclaimer

This script is provided as-is and is not affiliated with or endorsed by Blink or Amazon. Use at
