# 🚀 FastAPI Practices & Backend API Development

<p align="center">
  <a href="#english">English</a> | <a href="#türkçe">Türkçe</a>
</p>

---

## <a id="english"></a>🇬🇧 English

This repository contains structured FastAPI exercises, request validation practices, and RESTful API design patterns implemented in Python using Pydantic and Uvicorn.

### 📂 Repository Structure

- **[`Model-Schemas-And-Endpoints/`](./Model-Schemas-And-Endpoints/)**: RESTful API practice (`main.py`) featuring `StrEnum` model family routing (`llm`, `vision`, `tabular`), Pydantic request schemas (`InferenceRequest`, `ModelUpdate`), `Annotated` path/query parameter constraints (`Path`, `Query`), `dry_run` simulation logic, and `GET`, `POST`, and `PUT` endpoints verified via Swagger UI (`/docs`).

### 🛠 Tech Stack & Tools
- **Web Framework:** FastAPI
- **Data Validation:** Pydantic (`BaseModel`, `StrEnum`, `Annotated`)
- **ASGI Server:** Uvicorn
- **Language:** Python 3.11+
- **Version Control:** Git, GitHub, GitHub Desktop

---

## <a id="türkçe"></a>🇹🇷 Türkçe

Bu repo, Python, Pydantic ve Uvicorn kullanılarak geliştirilmiş yapılandırılmış FastAPI egzersizleri, istek doğrulama (request validation) pratikleri ve RESTful API tasarım desenlerini içermektedir.

### 📂 Depo Yapısı

- **[`Model-Schemas-And-Endpoints/`](./Model-Schemas-And-Endpoints/)**: `StrEnum` tabanlı model ailesi yönlendirmesi (`llm`, `vision`, `tabular`), Pydantic istek şemaları (`InferenceRequest`, `ModelUpdate`), `Annotated` ile yol/sorgu parametresi kısıtlamaları (`Path`, `Query`), `dry_run` simülasyon mantığı ve Swagger UI (`/docs`) üzerinden doğrulanan `GET`, `POST`, `PUT` uç noktalarını içeren RESTful API uygulaması (`main.py`).

### 🛠 Teknoloji Yığını ve Araçlar
- **Web Çatısı (Framework):** FastAPI
- **Veri Doğrulama:** Pydantic (`BaseModel`, `StrEnum`, `Annotated`)
- **ASGI Sunucusu:** Uvicorn
- **Programlama Dili:** Python 3.11+
- **Versiyon Kontrolü:** Git, GitHub, GitHub Desktop