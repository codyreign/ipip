# 🛡️ ipip File Operation Safety Guide

**ipip now has comprehensive safety measures to prevent moving system files and critical directories!**

## ✅ **What's Protected (NEVER Moved)**

### **🔒 Environment Directories**
- `venv/`, `.venv/`, `env/`, `.env/`
- `test_env/`, `dev_env/`, `prod_env/`
- `virtualenv/`, `conda_env/`, `pipenv/`
- `poetry_env/`, `.poetry/`

### **📁 Hidden Files & Directories**
- **All files/folders starting with `.`**
  - `.git/`, `.vscode/`, `.idea/`
  - `.gitignore`, `.env`, `.DS_Store`
  - `.cache/`, `.config/`, `.local/`

### **⚙️ System & Build Directories**
- `__pycache__/`, `.pytest_cache/`, `.coverage/`
- `node_modules/`, `.npm/`, `.yarn/`
- `build/`, `dist/`, `target/`, `out/`
- `.tox/`, `.nox/`, `htmlcov/`
- `site-packages/`, `lib64/`, `include/`

### **💻 IDE & Editor Files**
- `.vscode/`, `.idea/`, `.eclipse/`
- `.sublime-project`, `.atom/`, `.brackets/`
- Any IDE-specific configuration directories

### **📋 Critical Project Files**
- `setup.py`, `pyproject.toml`, `setup.cfg`
- `requirements.txt`, `Pipfile`, `package.json`
- `Makefile`, `Dockerfile`, `docker-compose.yml`
- `LICENSE`, `README.md`, `.gitignore`

### **🔐 Security & Config Files**
- `.env*` files (environment variables)
- `secrets.json`, `credentials.json`
- `config.ini`, `local_settings.py`
- Private keys, certificates

### **💾 Binary & Executable Files**
- `.exe`, `.dll`, `.so`, `.dylib`
- `.msi`, `.pkg`, `.deb`, `.rpm`
- `.bin`, `.dmg`, `.iso`, `.img`

### **🎬 Large Media Files**
- Video files: `.mp4`, `.avi`, `.mkv`, `.mov`
- Database files: `.db`, `.sqlite`, `.mdb`
- VM images: `.vmdk`, `.vdi`, `.ova`

## 🧪 **Testing the Safety System**

### **Safe Commands (These Work)**
```bash
# Only moves actual test files
ipip "move test files to tests folder" --dry-run

# Only moves documentation files
ipip "move doc files to docs folder" --dry-run

# Only moves specific installer scripts
ipip "move installer files to install folder" --dry-run
```

### **Protected Commands (These Are Safe)**
```bash
# Will NOT move your virtual environment
ipip "move all files to backup" --dry-run

# Will NOT move .git directory
ipip "organize project files" --dry-run

# Will NOT move setup.py or requirements.txt
ipip "move python files to src" --dry-run
```

## 📊 **What You'll See**

### **Safety Indicators**
```
🛡️  Safety: Automatically excluding system files, environments, and critical project files

📋 Planned File Operations
┌───────────┬────────────┬─────────┬──────────────────┬────────────┐
│ Operation │ Source     │ Target  │ Reason           │ Confidence │
├───────────┼────────────┼─────────┼──────────────────┼────────────┤
│ MOVE      │ test_1.py  │ tests   │ Move test file   │ 90.0%      │
│ MOVE      │ test_2.py  │ tests   │ Move test file   │ 90.0%      │
└───────────┴────────────┴─────────┴──────────────────┴────────────┘

ℹ️  847 files excluded for safety (environments, system files, etc.)
```

### **Verbose Mode Shows Exclusions**
```bash
ipip --verbose "move files" --dry-run
# Shows how many files were automatically excluded for safety
```

## 🚨 **Emergency Features**

### **Undo System**
```bash
# If something goes wrong, emergency undo!
ipip --undo
```

### **Always Use Dry Run First**
```bash
# ALWAYS test before actual execution
ipip --dry-run "any file command"
```

### **Safety Checks**
- **Preview before execution** - See exactly what will move
- **Confirmation prompts** - For any potentially dangerous operations
- **Operation logging** - All moves tracked for undo
- **Smart exclusions** - Automatically protects critical files

## 💡 **Pro Tips**

### **Be Specific**
```bash
# Good - specific and safe
ipip "move test files to tests folder"

# Avoid - too broad
ipip "move all files"
```

### **Check Exclusions**
```bash
# See what's being protected
ipip --verbose --dry-run "organize files"
```

### **Test First**
```bash
# Always dry-run first!
ipip --dry-run "move python files to src"
```

## 🎯 **Now 100% Safe!**

**Your critical files are protected:**
- ✅ Environment directories **WON'T** be moved
- ✅ Hidden system files **WON'T** be touched  
- ✅ Project configuration **WON'T** be relocated
- ✅ IDE settings **WON'T** be disturbed
- ✅ Binary/executable files **WON'T** be moved

**The AI is now intelligent enough to:**
- 🧠 Recognize system vs. user files
- 🛡️ Automatically exclude dangerous targets
- 📋 Show you exactly what's protected
- 🔄 Provide undo if needed

**No more DURKA DURKA chaos!** 🚀