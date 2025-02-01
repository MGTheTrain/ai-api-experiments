# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.4.0] - 01-02-2025

### Added

- [Feature] Desktop application designed to provide a user-friendly interface for interacting with OpenAI’s AIaaS web-backends enabling image generation, speech generation and chatting functionality
- Added script for formatting and linting

### Updated

- Renamed the project from `python-sample-apps-with-AIaaS-apis` to `ai-api-experiments` reflecting its expanded scope of additionally offering a desktop user interface for interacting with OpenAI’s AIaaS web-backends
- Organized applications into `desktop` and `cli` folders. Moved logic into separate files within the `src` folder and ensured they are reused across the applications 
- Reduce chat bot app complexity by removing option of having input prompt content in a file

### Removed 

- Removed the template folder and clarified that the `OPENAI_API_KEY` must be exported in `README.md's`
- Removed version file and CI workflow

## [0.3.0] - 20-04-2024

### Added

- [Feature] Speech generator CLI Tool utilizing tts-1 or tts-1-hd model

### Updated

- Update formatting in `README.md for Starting application section`

## [0.2.0] - 20-04-2024

### Added

- [Feature] Image generator CLI Tool utilizing dall-e-2 or dall-e-3 model

## [0.1.0] - 20-04-2024

### Added

- Initial project setup
- [Feature] Chat bot CLI Tool utilizing gpt-3.5-turbo or gpt-4-turbo model