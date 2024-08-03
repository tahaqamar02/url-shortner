# URL Shortener

## Overview

This Python application provides a utility for shortening long URLs using multiple URL shortening services. It supports TinyURL, Bitly, is.gd, and Osdb. The user can select a service and input a long URL to receive a shortened URL. The application is designed to handle errors gracefully and supports multiple URL shortening operations within a single session.

## Features

- **Multiple Services**: Shorten URLs using TinyURL, Bitly, is.gd, and Osdb.
- **Bitly Integration**: Supports authentication with a Bitly API key for enhanced functionality.
- **Error Handling**: Includes robust error handling for invalid inputs and API errors.
- **Session Management**: Enables users to shorten multiple URLs in a single session.

## Requirements

- **Python 3.x**: Ensure you have Python 3.x installed on your system.
- **pyshorteners**: A Python library for interacting with URL shortening services.
- **(Optional) pyperclip**: A Python library for clipboard operations, useful for automatically copying shortened URLs.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/url-shortener.git
   cd url-shortener
