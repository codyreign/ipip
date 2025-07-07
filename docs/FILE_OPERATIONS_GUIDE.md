# 📁 ipip File Operations Guide

ipip now supports intelligent file operations using AI to understand and execute complex file management tasks.

## 🚀 **New Capabilities**

### **Intelligent File Analysis**
- Automatically categorizes files (test, source, config, docs, etc.)
- Understands file purposes and relationships
- Detects project structure patterns

### **Natural Language Commands**
- Use plain English to describe file operations
- AI interprets complex multi-step tasks
- Safe execution with confirmation prompts

## 📋 **File Operation Commands**

### **Create Files and Folders**

```bash
# Create folders
ipip "create a tests folder"
ipip "create docs and assets directories"
ipip "create folder called config"

# Create files with content
ipip "create file 'README.md' with content 'Hello World'"
ipip "create 'main.py' containing import statements"
```

### **Move and Organize Files**

```bash
# Move by file type
ipip "move all test files to a tests folder"
ipip "organize python files into src folder"
ipip "move config files to config directory"

# Complex organization
ipip "move all test files to a test folder"
ipip "organize documentation files"
ipip "move all images to an assets folder"
ipip "group all scripts together"
```

### **Copy Operations**

```bash
# Copy files
ipip "copy all python files to backup folder"
ipip "copy configuration files to config-backup"
ipip "duplicate test files for experimentation"
```

### **Delete Operations** (Safe)

```bash
# Only allows deletion of safe file types
ipip "delete temporary files"
ipip "remove build artifacts"
ipip "clean up temp files"

# Requires confirmation for other deletions
ipip "delete old log files"
```

## 🎯 **Real-World Examples**

### **Example 1: Organize a Messy Project**

**Command:**
```bash
ipip "move all test files to a test folder"
```

**What happens:**
1. 🔍 Analyzes all files in current directory
2. 🏷️ Identifies test files (test_*.py, *_test.js, etc.)
3. 📁 Creates `tests/` folder if it doesn't exist
4. 📋 Shows preview of operations
5. ✅ Moves files after confirmation

**Expected output:**
```
📋 Planned File Operations
┌───────────┬──────────────┬─────────┬────────────────────┬────────────┐
│ Operation │ Source       │ Target  │ Reason             │ Confidence │
├───────────┼──────────────┼─────────┼────────────────────┼────────────┤
│ CREATE    │ —            │ tests   │ Create tests folder│ 90.0%      │
│ MOVE      │ test_main.py │ tests   │ Move test file     │ 90.0%      │
│ MOVE      │ auth_test.py │ tests   │ Move test file     │ 90.0%      │
└───────────┴──────────────┴─────────┴────────────────────┴────────────┘

Some operations are potentially destructive. Continue? [y/N]: y
✅ 3 operation(s) completed successfully
```

### **Example 2: Project Structure Setup**

**Command:**
```bash
ipip "create folders for docs, tests, config, and assets"
```

**What happens:**
1. 📁 Creates `docs/`, `tests/`, `config/`, `assets/` directories
2. 📋 Shows what will be created
3. ✅ Creates all folders

### **Example 3: Clean Up Build Files**

**Command:**
```bash
ipip "delete build files and temporary files"
```

**What happens:**
1. 🔍 Finds *.pyc, __pycache__, build/, dist/, temp files
2. 📋 Shows what will be deleted (safe files only)
3. 🗑️ Removes files after confirmation

## 🛡️ **Safety Features**

### **Confirmation Prompts**
- Shows preview of all operations before execution
- Requires confirmation for destructive operations
- Dry-run mode available with `--dry-run`

### **Smart File Detection**
- Only deletes "safe" file types by default (temp, build artifacts)
- Won't delete source code without explicit confirmation
- Analyzes file relationships before moving

### **Rollback Information**
- Tracks all file movements
- Shows exactly what was changed
- Clear error messages if operations fail

## 🔧 **Advanced Usage**

### **Dry Run Mode**
```bash
# See what would happen without actually doing it
ipip --dry-run "move all test files to tests folder"
```

### **Verbose Mode**
```bash
# See detailed analysis and decision process
ipip --verbose "organize python files"
```

### **Complex Multi-Step Operations**
```bash
# AI handles complex requests
ipip "organize this project with proper folder structure for tests, docs, config, and source code"
```

## 🎯 **File Categories Detected**

| Category | Examples | Auto-organize to |
|----------|----------|------------------|
| **Test** | test_*.py, *_test.js, *.spec.ts | `tests/` |
| **Documentation** | *.md, README, docs/ | `docs/` |
| **Configuration** | *.json, *.yaml, .env | `config/` |
| **Scripts** | *.sh, *.bat, scripts/ | `scripts/` |
| **Assets** | *.png, *.css, assets/ | `assets/` |
| **Data** | *.csv, *.json, data/ | `data/` |
| **Build** | *.pyc, dist/, __pycache__ | *delete* |
| **Source** | *.py, *.js, *.java | `src/` |

## 💡 **Tips and Best Practices**

### **Use Descriptive Commands**
```bash
# Good
ipip "move all python test files to a tests directory"

# Less clear
ipip "move files"
```

### **Start with Dry Run**
```bash
# Always test first
ipip --dry-run "organize all files by type"
```

### **Combine with Package Operations**
```bash
# Install packages, then organize
ipip "flask for web development"
ipip "create project structure with templates and static folders"
```

## 🚨 **Important Notes**

1. **Always backup important files** before major reorganization
2. **Use `--dry-run`** to preview operations
3. **File operations respect .gitignore** patterns
4. **Deletions are limited to safe file types** by default
5. **Complex operations may require confirmation**

## 🎉 **Ready to Use**

File operations are now integrated into ipip! Try these commands:

```bash
# Quick test
ipip --dry-run "create a tests folder"

# Real organization
ipip "move all test files to tests folder"

# Project setup
ipip "create proper project structure"
```

Your intelligent file manager is ready! 🚀