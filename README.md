# ipip - Intelligent Pip Package Installer

[![PyPI version](https://badge.fury.io/py/ipip.svg)](https://badge.fury.io/py/ipip)
[![Python versions](https://img.shields.io/pypi/pyversions/ipip.svg)](https://pypi.org/project/ipip/)
[![Downloads](https://pepy.tech/badge/ipip)](https://pepy.tech/project/ipip)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/codyreign/ipip/workflows/Test%20Package/badge.svg)](https://github.com/codyreign/ipip/actions)

**ipip** is an intelligent pip package installer that uses AI to understand what you want and automatically handles package resolution, file organization, and project management. Just install and go - no configuration needed!

## Features

🧠 **Intelligent Package Resolution**: Uses LLM to understand what package you actually want
- `ipip blender` → installs `bpy`
- `ipip pil` → installs `pillow`
- `ipip opencv` → installs `opencv-python`

🔍 **Smart Package Discovery**: Find packages by describing what you need
- `ipip vision recognition` → shows computer vision packages
- `ipip machine learning` → shows ML libraries
- `ipip web scraping` → shows web scraping tools

📁 **Intelligent File Operations**: AI-powered file management and organization
- `ipip "move all test files to tests folder"` → analyzes and organizes files
- `ipip "create project structure"` → sets up proper folder hierarchy
- `ipip "delete temporary files"` → safely removes build artifacts
- `ipip "list installer files"` → finds and displays files intelligently
- `ipip "move files to scripts folder"` → works with files from previous context

🧠 **Conversational File Context**: Remembers your previous file operations
- List files, then move them: `ipip "list installer files"` → `ipip "move files to folder"`
- AI remembers active files between commands for seamless workflow
- Context-aware operations: files from previous lists are automatically included

🛡️ **Advanced Safety Features**: Protects your system and project files
- **Smart Exclusions**: Automatically excludes environments, system files, .git, node_modules
- **Emergency Undo**: Comprehensive logging and rollback of file operations
- **Safety Confirmations**: Warns before destructive operations
- **AI File Matching**: Uses complete file hierarchy for intelligent pattern recognition

📝 **Dynamic Requirements Management**: Automatically manage your project dependencies
- `ipip create requirements` → generates requirements.txt from your project
- `ipip update requirements` → updates existing requirements file

🚀 **Natural Language Commands**: Commands are dynamic and LLM-based
- `ipip requirements file`
- `ipip create requirements file`
- `ipip organize python files`

All work the same way!

## Installation

### 🚀 One-Line Install (Recommended)

**From PyPI (Recommended):**
```bash
pip install ipip
```

**One-Line Installers:**

**Windows:**
```cmd
curl -o install.bat https://raw.githubusercontent.com/codyreign/ipip/main/install.bat && install.bat
```

**Unix/Linux/macOS:**
```bash
curl -sSL https://raw.githubusercontent.com/codyreign/ipip/main/install.sh | bash
```

**✨ What happens automatically:**
- ✅ Installs ipip and dependencies
- ✅ Detects/installs Ollama (local AI)
- ✅ Downloads AI model (llama3.2)
- ✅ Tests everything works
- ✅ Ready to use immediately!

### Alternative Methods

**From GitHub (Development):**
```bash
pip install git+https://github.com/codyreign/ipip.git
ipip --setup  # Run first-time setup
```

## Usage

### Basic Package Installation

```bash
# Install packages using common names
ipip blender          # Installs bpy for Blender Python API
ipip pil             # Installs pillow for image processing
ipip opencv          # Installs opencv-python
ipip sklearn         # Installs scikit-learn
```

### Package Discovery

```bash
# Find packages for specific domains
ipip vision recognition        # Shows computer vision packages
ipip machine learning         # Shows ML libraries
ipip web development api      # Shows API frameworks
ipip database tools          # Shows database libraries
```

### File Operations

```bash
# List and discover files intelligently
ipip "list installer files"                    # Finds all files with install/installer patterns
ipip "list all python files"                   # Lists Python source files
ipip "list config files"                       # Shows configuration files
ipip "list files with 'test' in name"         # Custom pattern matching

# Organize files intelligently
ipip "move all test files to tests folder"     # Moves test files to tests/
ipip "create project structure with docs and config folders"  # Creates folder structure
ipip "organize python files by type"          # Organizes by file purpose

# Conversational workflow (files remembered between commands)
ipip "list installer files"                   # Lists files and remembers them
ipip "move files to scripts folder"           # Moves the previously listed files

# Create files and folders
ipip "create README.md with project description"  # Creates file with content
ipip "create folders for tests, docs, and config"  # Creates multiple folders

# Clean up safely (with confirmations)
ipip "delete temporary files"                  # Safely removes temp files
ipip "remove build artifacts"                  # Cleans build outputs
```

### File Context Management

```bash
# Show current file context
ipip --context                                 # Shows active files from previous operations
ipip --clear-context                          # Clears current file context

# File operations work with context
ipip "list config files"                      # Step 1: List files
ipip "move files to config folder"            # Step 2: Move the listed files
ipip "copy files to backup"                   # Step 3: Copy the same files
```

### Requirements Management

```bash
# Generate requirements.txt from your project
ipip create requirements
ipip generate requirements file
ipip requirements

# Update existing requirements.txt
ipip update requirements
ipip refresh requirements file
```

### Advanced Options

```bash
# Dry run (see what would be installed)
ipip --dry-run blender

# Verbose output
ipip --verbose opencv

# Use different LLM model
ipip --model openai package-name

# File context options
ipip --context                                 # Show current file context
ipip --clear-context                          # Clear current file context

# Emergency file operations
ipip undo                                      # Undo last 10 file operations
ipip undo --count 5                           # Undo last 5 operations
```

## Configuration

ipip can be configured using a config file or environment variables.

### Config File

The config file is located at:
- **Linux/macOS**: `~/.config/ipip/config.json`
- **Windows**: `%APPDATA%/ipip/config.json`

Example configuration:

```json
{
  "llm": {
    "model": "local",
    "api_key": "",
    "api_url": "",
    "timeout": 30,
    "max_retries": 3,
    "temperature": 0.1
  },
  "verbose": false,
  "dry_run_default": false,
  "auto_confirm": false,
  "requirements_filename": "requirements.txt",
  "exclude_system_packages": true,
  "package_search_limit": 10
}
```

### Environment Variables

- `IPIP_MODEL`: Override the LLM model
- `IPIP_API_KEY`: Set API key for remote models
- `IPIP_API_URL`: Set API URL for remote models
- `IPIP_TIMEOUT`: Set request timeout

### Local LLM Setup

ipip works best with a local LLM like Ollama:

1. Install [Ollama](https://ollama.ai/)
2. Pull a model: `ollama pull llama3.2`
3. ipip will automatically use the local model

## How it Works

### Package Installation
1. **Intent Parsing**: ipip uses LLM to understand what you want to do
2. **Package Resolution**: Combines LLM intelligence with curated mappings
3. **Smart Installation**: Installs the correct packages with proper error handling
4. **Project Analysis**: For requirements generation, scans your code for imports

### File Operations
1. **AI Analysis**: Analyzes your entire project structure and file purposes
2. **Context Memory**: Remembers files from previous operations for conversational workflow
3. **Safety First**: Automatically excludes system files, environments, and critical project files
4. **Smart Matching**: Uses AI to understand file patterns and relationships
5. **Operation Preview**: Shows what will happen before executing destructive operations
6. **Emergency Recovery**: Logs all operations with full undo capabilities

### Safety Exclusions
ipip automatically protects these critical files and directories:
- **Hidden files**: `.git`, `.vscode`, `.idea`, `.env*`
- **Virtual environments**: `venv`, `env`, `node_modules`, `__pycache__`
- **System files**: `Thumbs.db`, `.DS_Store`, `desktop.ini`
- **Critical project files**: `setup.py`, `requirements.txt`, `package.json`
- **Build artifacts**: `dist/`, `build/`, `target/`, `*.pyc`
- **Large binaries**: `*.exe`, `*.dll`, `*.so`, `*.dmg`

## Examples

### Install Computer Vision Stack

```bash
ipip computer vision
# Installs: opencv-python, pillow, scikit-image
```

### Install Machine Learning Environment

```bash
ipip machine learning
# Installs: scikit-learn, pandas, numpy, matplotlib
```

### Install Web Development Tools

```bash
ipip web api development
# Shows: fastapi, flask, django-rest-framework
```

### Project Requirements

```bash
# In your project directory
ipip create requirements
# Analyzes your code and creates requirements.txt
```

### File Organization Examples

```bash
# Organize a messy project
ipip "list all files"                          # See what's in your project
ipip "create folders for tests, docs, scripts" # Set up structure
ipip "move test files to tests"               # Organize test files
ipip "move documentation to docs"             # Organize docs
ipip "move installer files to scripts"        # Move installer scripts

# Clean up after development
ipip "list temporary files"                   # See what can be cleaned
ipip "delete build artifacts"                 # Remove compiled files
ipip "remove temp files"                      # Clean temporary files
```

### Conversational Workflow Example

```bash
# Step 1: Discover files
ipip "list installer files"
# Output: Found 3 files: install.bat, install.sh, quick_install.bat

# Step 2: Work with those files (they're remembered)
ipip "move files to scripts folder"
# Moves the 3 installer files to scripts/

# Step 3: Continue working with same files
ipip "copy files to backup"
# Copies the same 3 files to backup/

# Step 4: Check what happened
ipip --context
# Shows the current active files and operations
```

## Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/codyreign/ipip.git
cd ipip

# Install in development mode
make install-dev

# Or manually
pip install -e .
```

### Available Make Commands

```bash
make help           # Show all available commands
make install        # Install ipip system-wide
make install-dev    # Install in development mode
make build          # Build package
make clean          # Clean build artifacts
make test           # Run tests
make lint           # Run linting
make format         # Format code
make uninstall      # Uninstall ipip
```

### Running Tests

```bash
make test
# Or manually:
pytest tests/
```

### Code Quality

```bash
make format         # Format code
make lint          # Run linting

# Or manually:
black ipip/ tests/
flake8 ipip/ tests/
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Troubleshooting

### Common Issues

**File operations not working:**
- Check if you're in the correct directory
- Use `ipip --verbose` to see detailed output
- Verify Ollama is running: `ollama list`

**AI not understanding queries:**
- Try different wording: "list installer files" vs "show files with install"
- Use `ipip --verbose` to see AI analysis
- Check if you have a suitable LLM model installed

**Undo not working:**
- Emergency undo only works for recent operations
- Use `ipip undo --count 20` to undo more operations
- Check operation logs in your config directory

**Package resolution issues:**
- Some packages may need specific models (avoid LLaVA for text queries)
- Try `ipip --model llama3.2` for better text understanding
- Use `ipip --dry-run` to preview without installing

### Getting Help

```bash
ipip --help                    # Show all available options
ipip --verbose "your command"  # Debug mode with detailed output
```

## Roadmap

- [ ] Support for more LLM providers (OpenAI, Anthropic, etc.)
- [ ] Package similarity detection
- [ ] Integration with virtual environment managers
- [ ] Web interface for package discovery
- [ ] Package recommendation based on project analysis
- [ ] Support for conda packages
- [ ] Plugin system for custom resolvers
- [ ] Advanced file operation patterns and templates
- [ ] Project-specific safety rule customization
- [ ] Batch operations and operation scheduling

## Acknowledgments

- Inspired by the need for smarter package management
- Built with [Click](https://click.palletsprojects.com/) for CLI
- Uses [Rich](https://github.com/Textualize/rich) for beautiful terminal output
- LLM integration supports [Ollama](https://ollama.ai/) for local inference