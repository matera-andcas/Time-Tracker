# Como Distribuir o Time Tracker

## 🎯 Opções de Distribuição

### 1. **Executável Standalone (Recomendado)**

#### Criar o executável:
```bash
./build.sh
```

Isso criará um arquivo único em `dist/TimeTracker` (~50-80 MB) que pode ser distribuído.

#### Distribuir:
```bash
# Apenas envie este arquivo
dist/TimeTracker
```

**Vantagens:**
- ✅ Um único arquivo
- ✅ Não precisa instalar Python
- ✅ Não precisa instalar dependências
- ✅ Funciona em qualquer Linux x64

**Desvantagens:**
- ⚠️ Arquivo grande (~50-80 MB)
- ⚠️ Específico para arquitetura (x64)

---

### 2. **AppImage (Portável)**

```bash
# Instalar appimagetool
wget https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage
chmod +x appimagetool-x86_64.AppImage

# Criar estrutura
mkdir -p TimeTracker.AppDir/usr/bin
cp dist/TimeTracker TimeTracker.AppDir/usr/bin/
cp timetracker.desktop TimeTracker.AppDir/

# Criar AppImage
./appimagetool-x86_64.AppImage TimeTracker.AppDir
```

**Resultado:** `TimeTracker-x86_64.AppImage`
- Clique duplo para executar
- Funciona em qualquer distribuição

---

### 3. **Distribuir Código Fonte**

```bash
# Criar arquivo compactado
tar -czf timetracker.tar.gz \
    --exclude='venv' \
    --exclude='__pycache__' \
    --exclude='*.db' \
    .
```

**Usuário final executa:**
```bash
tar -xzf timetracker.tar.gz
cd timeTracker
./install.sh
./run.sh
```

---

### 4. **Pacote .deb (Ubuntu/Debian)**

```bash
# Estrutura
mkdir -p timetracker_1.0/DEBIAN
mkdir -p timetracker_1.0/usr/bin
mkdir -p timetracker_1.0/usr/share/applications

# Copiar arquivos
cp dist/TimeTracker timetracker_1.0/usr/bin/
cp timetracker.desktop timetracker_1.0/usr/share/applications/

# Criar control
cat > timetracker_1.0/DEBIAN/control << EOF
Package: timetracker
Version: 1.0
Architecture: amd64
Maintainer: Seu Nome <email@example.com>
Description: Aplicação de time tracking
Depends: libxcb-cursor0
EOF

# Criar pacote
dpkg-deb --build timetracker_1.0
```

**Instalar:**
```bash
sudo dpkg -i timetracker_1.0.deb
```

---

## 📋 Comparação

| Método | Tamanho | Instalação | Compatibilidade |
|--------|---------|------------|-----------------|
| Executável | ~60 MB | Nenhuma | Linux x64 |
| AppImage | ~60 MB | Chmod +x | Todas distros |
| Código fonte | ~100 KB | ./install.sh | Python 3.8+ |
| .deb | ~60 MB | dpkg -i | Ubuntu/Debian |

---

## 🚀 Método Recomendado

Para distribuição rápida, use o **executável standalone**:

```bash
# No seu computador
./build.sh

# Enviar para os outros
scp dist/TimeTracker usuario@servidor:/caminho/
# ou via pendrive, email, etc.

# Outros usuários executam
chmod +x TimeTracker
./TimeTracker
```

---

## ⚠️ Notas Importantes

### Banco de Dados
O banco `timetracker.db` é criado automaticamente no diretório onde o executável rodar.

### Dependências do Sistema
O executável ainda precisa de algumas bibliotecas do sistema:
- `libxcb` (X11)
- `libfontconfig`
- `libfreetype`

Geralmente já estão instaladas em qualquer desktop Linux.

### Testar em VM
Antes de distribuir, teste em uma máquina virtual limpa:
```bash
# Em VM Ubuntu limpa
./TimeTracker
# Se funcionar, está OK para distribuir
```

---

## 🔧 Build Avançado

### Reduzir tamanho do executável:
```bash
pyinstaller --onefile \
    --windowed \
    --strip \
    --exclude-module matplotlib \
    --exclude-module numpy \
    main.py
```

### Adicionar ícone:
```bash
pyinstaller --onefile \
    --windowed \
    --icon=icon.ico \
    main.py
```

---

## 📦 Checklist de Distribuição

- [ ] Executar `./build.sh`
- [ ] Testar `dist/TimeTracker` localmente
- [ ] Testar em VM limpa
- [ ] Verificar tamanho do arquivo
- [ ] Criar README com instruções
- [ ] Enviar/compartilhar arquivo
- [ ] Instruir usuários: `chmod +x TimeTracker && ./TimeTracker`

---

**Última atualização:** 19/01/2026
