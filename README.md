# Weblish

**Weblish** is a lightweight JavaScript extension that allows developers to write natural language (English) instructions within HTML using `<script type="text/english">`, which are then dynamically compiled into executable JavaScript using Google Gemini.

---

## Features

- 🔤 Write logic in English inside HTML.
- ⚙️ Translates natural language to JavaScript on the fly.
- 🌐 FastAPI backend with Gemini 2.0 Flash support.
- 🧠 LLM-powered code generation.
- 💡 CORS-enabled for client-side integration.
- ✅ Pluggable and extensible runtime design.

---

## Table of Contents

- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [Security Notice](#security-notice)
- [License](#license)

---

## Project Structure

```
.
├── browser/
│   └── bridge.js          # Client-side script loader and runtime
├── example.html           # Demo page using <script type="text/english">
├── main.py                # FastAPI backend and compiler logic
├── requirements.txt       # Backend dependencies
└── .env                   # Local environment variables (not tracked)
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- [Google Generative AI API Key](https://aistudio.google.com/app/apikey)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/ByteJoseph/weblish.git
```

```
cd weblish
```

2. Create and configure your `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the server:

```bash
uvicorn main:app --reload
```

The backend will be available at `http://127.0.0.1:8000/`.

---

## Usage

Embed Weblish into your HTML page:

```html
<script src="https://weblish.onrender.com"></script>

<script type="text/english">
  show hi on the screen as an alert // write your instructions here
</script>
```

> This sends "show hi on the screen as an alert" to the backend, which returns and executes corresponding JavaScript code via `eval()`.

### Remote Usage (Deployed):

```html
<script src="https://weblish.onrender.com"></script>
```

---

## API Endpoints

| Method | Endpoint           | Description                                |
| ------ | ------------------ | ------------------------------------------ |
| GET    | `/`                | Returns minified `bridge.js` client script |
| GET    | `/compile?script=` | Compiles natural language to JavaScript    |
| GET    | `/health`          | Health check                               |
| GET    | `/license`         | Returns the license file content           |

---

## Contributing

Contributions are welcome and encouraged! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Make your changes
4. Commit your changes (`git commit -m "Add feature"`)
5. Push to the branch (`git push origin feature-name`)
6. Open a pull request

### Guidelines

- Follow consistent code style
- Document public functions and endpoints
- Avoid breaking existing functionality

---

## Security Notice

> ⚠️ **Important:**  
> This project executes LLM-generated code using `eval()` inside the browser. **Do not** use in production environments or with untrusted input.

Use only in educational, experimental, or sandboxed scenarios.

---

## License

See [`LICENSE`](./LICENSE) or access it via the `/license` endpoint.

---

## Maintainers

- [ByteJoseph](https://github.com/ByteJoseph) – Creator & Maintainer
