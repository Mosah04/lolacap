# Lolacap

Lolacap is an AI-powered solution designed to translate and subtitle audiovisual content into local languages. Its primary goal is to make multimedia content accessible to broader audiences by breaking language barriers and promoting inclusivity.

## Features

- **Automated Transcription**: Lolacap automatically transcribes audio from various video formats.
- **AI Translation**: Translates transcribed text into a wide range of local languages using state-of-the-art AI models.
- **Subtitling**: Generates synchronized subtitles for videos, preserving timing and accuracy.
- **User-Friendly Interface**: Designed to allow easy upload and processing of audiovisual materials.
- **Extensible**: Built with Python, making it easy to extend, integrate, and contribute to.

## Use Cases

- Making educational, entertainment, or informational videos accessible to speakers of local languages.
- Localizing content for different regions.
- Supporting accessibility for deaf and hard-of-hearing communities.

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Mosah04/lolacap.git
   cd lolacap
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   > **Note:** Please ensure you have Python 3.7 or higher installed.

## Usage

Depending on the available scripts, you can typically use Lolacap via command line. A general usage pattern might look like:

```bash
python main.py --input path/to/video.mp4 --output path/to/output.srt --language yoruba
```

- `--input`: Path to your input video file.
- `--output`: Path for the generated subtitle file.
- `--language`: Target local language for translation (e.g., yoruba, hausa, igbo).

> Refer to the documentation or inline help (`python main.py --help`) for all options and supported languages.

## Contributing

Contributions are welcome! Please:
- Open an issue to discuss improvements or report bugs.
- Fork the repo and submit a pull request.
- Follow standard Python coding conventions.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Inspired by the need for accessible content in local African languages.
- Powered by open-source AI and speech-to-text technologies.

---

**LolaCap** — Breaking language barriers, one subtitle at a time.
