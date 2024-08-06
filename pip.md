
# 🐍 Pip Commands! 🎉

## 🚀 Basic Commands
### **Install a package**: 
```bash 
pip install package_name
```
---
### **Upgrade a package**: 
```bash
pip install --upgrade package_name
```
### **Uninstall a package**: 
```bash 
pip uninstall package_name
```
---
## 🔍 Searching & Listing
### **Search for a package**:
```bash
pip search search_term
```
---
### **List installed packages**:
```bash
pip list
```
---
### **Show package details**:
```bash
pip show package_name
```
---
## 📦 Freezing & Requirements
### **Freeze installed packages**:
```bash
pip freeze
```
---
### **Save installed packages to a file**:
```bash
pip freeze > requirements.txt
```
---
### **Install from a requirements file**:
```bash
pip install -r requirements.txt
```
---
## 🛠️ Advanced Commands
### **Check for outdated packages**:
```bash
pip list --outdated
```
---
### **Upgrade all outdated packages**:
```bash
pip install --upgrade $(pip list --outdated | awk 'NR>2 {print $1}')
```
---
### **Install a specific version**:
```bash
pip install package_name==version
```
---
### **Install from a URL**:
```bash
pip install https://example.com/package.tar.gz
```
---
### **Install from a local directory**:
```bash
pip install ./path/to/package
```
---
## 🌟 Useful Tips
### **Install with extras**:
```bash
pip install package_name[extra]
```
---
### **Use a different index**:
```bash
pip install package_name --index-url http://custom.index/simple/
```
---
### **Install in user site**:
```bash
pip install --user package_name
```
---
### **Show help for pip**:
```bash
pip help
```
---
# 🐍
