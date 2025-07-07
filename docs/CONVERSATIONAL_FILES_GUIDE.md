# 🗣️ ipip Conversational File Operations Guide

**ipip now supports conversational file operations with intelligent context management!**

## 🧠 **How Context Works**

ipip remembers the files you're working with, making operations more natural and conversational.

### **Context is Created When:**
- 📋 **Listing files**: `ipip "list installer files"`
- 📄 **Creating files**: `ipip "create file app.py"`
- 📁 **Working with files**: Any file operation

### **Context is Used When:**
- 🔄 **Referencing files**: `ipip "move files to new folder"`
- 🗂️ **Continuing work**: `ipip "copy them to backup"`

## 📋 **File Listing Commands**

### **List Specific File Types**
```bash
# List by category
ipip "list installer files"
ipip "list test files"  
ipip "list python files"
ipip "list config files"

# List by pattern
ipip "show .py files"
ipip "find documentation files"
ipip "display image files"
```

### **Expected Output**
```
📁 Files matching 'installer files' (3 found):

🔧 install.bat          Installer script         2KB
🔧 install.sh           Installer script         1KB  
🔧 quick_install.bat    Installer script         1KB

💡 These files are now in your active context. Use commands like 'move files to folder' to work with them.
```

## 🔄 **Conversational Operations**

### **Workflow Example 1: Organizing Installers**

```bash
# Step 1: List the files
ipip "list installer files"
# → Shows 3 installer files, adds them to context

# Step 2: Work with those files (no need to specify again!)
ipip "move files to install folder"
# → Creates 'install' folder and moves the 3 installer files

# Step 3: Continue working
ipip "copy them to backup folder too"
# → Copies the same files to backup folder
```

### **Workflow Example 2: Creating and Working with Files**

```bash
# Step 1: Create a file
ipip "create file app.py"
# → Creates app.py, sets it as active context

# Step 2: Work with the file
ipip "move file to src folder"
# → Moves app.py to src/ folder

# Step 3: Create more files
ipip "create file test_app.py"
# → Creates test file, updates context to just this file
```

### **Workflow Example 3: Multiple File Types**

```bash
# List multiple types
ipip "list test files"
# → Shows all test files, sets context

# Later, start fresh with different files
ipip "list config files"  
# → Clears old context, shows config files, sets new context

# Work with the config files
ipip "organize files by type"
# → Organizes the config files that were just listed
```

## 🎯 **Context-Aware Commands**

### **Commands That Use Context**
- `"move files"`
- `"copy files"`
- `"move them"`
- `"copy them"`
- `"delete files"`
- `"organize files"`
- `"these files"`
- `"the files"`
- `"current files"`
- `"active files"`

### **Commands That Start Fresh Context**
- `"list ..."` / `"show ..."` / `"find ..."`
- `"create file ..."` / `"create folder ..."`

## 🛠️ **Context Management Commands**

### **View Current Context**
```bash
# Show what files are currently active
ipip --context

# Show detailed context info
ipip --verbose --context
```

### **Clear Context**
```bash
# Start fresh (clear active files)
ipip --clear-context
```

### **Context in Operations**
```bash
# See context being used (verbose mode)
ipip --verbose "move files to backup"
```

## 📊 **Context Display**

### **Simple Context View**
```
📁 Active file context (3 files):
🔧 install.bat         exists
🔧 install.sh          exists  
🔧 quick_install.bat   exists
```

### **Detailed Context View** (with `--verbose`)
```
📁 Active file context (3 files):
Last operation: list installer files
Operation type: list
Timestamp: 2024-07-07T16:30:45

🔧 install.bat         exists
🔧 install.sh          exists
🔧 quick_install.bat   exists
```

## 💡 **Smart Examples**

### **Example 1: Project Organization**
```bash
# Start by exploring
ipip "list python files"

# Organize them
ipip "move files to src folder"

# Work with tests next
ipip "list test files"

# Organize tests
ipip "move files to tests folder"
```

### **Example 2: File Creation Workflow**
```bash
# Create main file
ipip "create file main.py"

# Main.py is now active, work with it
ipip "move file to src folder"

# Create config
ipip "create file config.json"

# Config.json is now active (replaced main.py in context)
ipip "move file to config folder"
```

### **Example 3: Batch Operations**
```bash
# Find all markdown files
ipip "list documentation files"

# Move them all
ipip "move files to docs folder"

# Copy them for backup
ipip "copy files to backup/docs folder"
```

## 🔍 **Context Behavior**

### **Context Persistence**
- ✅ **Survives between commands** - Context saved to disk
- ✅ **Restored on restart** - Remembers your last work
- ✅ **Smart updates** - New operations update context

### **Context Clearing**
- 🔄 **Automatic**: When listing new files
- 🔄 **Manual**: `ipip --clear-context`
- 🔄 **On create**: Creating files sets new single-file context

### **Safety Features**
- 🛡️ **File validation**: Only works with existing files
- 🛡️ **Smart filtering**: Excludes system/environment files
- 🛡️ **Preview mode**: Shows what will happen before doing it

## 🎯 **Pro Tips**

### **Be Conversational**
```bash
# Instead of repeating file specifications
ipip "list installer files"
ipip "move installer files to install folder"  # ❌ Repetitive

# Be conversational
ipip "list installer files"
ipip "move them to install folder"  # ✅ Natural
```

### **Use Context Commands**
```bash
# Check what you're working with
ipip --context

# Start fresh when needed
ipip --clear-context
```

### **Combine with Verbose Mode**
```bash
# See exactly what's happening
ipip --verbose "move files to backup"
```

## 🚀 **Ready to Use!**

**Conversational file operations are now active:**

- 📋 **List files**: `ipip "list installer files"`
- 🧠 **Remember context**: Automatically tracks your files
- 🗣️ **Be conversational**: `ipip "move them to new folder"`
- 🔄 **Continue working**: Context flows between commands
- 🛠️ **Manage context**: `--context`, `--clear-context`

**Your AI assistant now has memory for much more natural file management!** 🎉