# 🚀 FastAPI Practices & Backend API Development

<p align="center">
  <a href="#english">English</a> | <a href="#türkçe">Türkçe</a>
</p>

---

## <a id="english"></a>🇬🇧 English

This repository contains structured FastAPI exercises, request validation practices, and RESTful API design patterns implemented in Python using Pydantic and Uvicorn.

### 📂 Repository Structure

- **[`Model-Schemas-And-Endpoints/`](./Model-Schemas-And-Endpoints/)**: RESTful API practice (`main.py`) featuring `StrEnum` model family routing (`llm`, `vision`, `tabular`), Pydantic request schemas (`InferenceRequest`, `ModelUpdate`), `Annotated` path/query parameter constraints (`Path`, `Query`), `dry_run` simulation logic, and `GET`, `POST`, and `PUT` endpoints verified via Swagger UI (`/docs`).
- **[`Task-And-Model-Hub-API/`](./Task-And-Model-Hub-API/)**: User registration and profile filtering (`response_model=UserBase`, `response_model_exclude_unset=True`), nested task schemas (`TaskCreate`, `TaskUpdate`, `EvidenceImage` with `HttpUrl` and `set[str]`), `openapi_examples` (`normal_gorev`, `kritik_ariza`), `dict[int, float]` weights, `Body(embed=True)` with `dry_run` updates, `204 No Content` deletion, and dual-mode `/health-raw` endpoint.

### 🛠 Tech Stack & Tools
- **Web Framework:** FastAPI (`Path`, `Body`, `Response`, `JSONResponse`, `status`)
- **Data Validation:** Pydantic v2 (`BaseModel`, `Field`, `EmailStr`, `HttpUrl`, `StrEnum`, `Annotated`)
- **ASGI Server:** Uvicorn
- **Language:** Python 3.11+
- **Storage:** In-memory dictionaries (`dict`)
- **Version Control:** Git, GitHub, GitHub Desktop

---

## <a id="türkçe"></a>🇹🇷 Türkçe

Bu repo, Python, Pydantic ve Uvicorn kullanılarak geliştirilmiş yapılandırılmış FastAPI egzersizleri, istek doğrulama (request validation) pratikleri ve RESTful API tasarım desenlerini içermektedir.

### 📂 Depo Yapısı

- **[`Model-Schemas-And-Endpoints/`](./Model-Schemas-And-Endpoints/)**: `StrEnum` tabanlı model ailesi yönlendirmesi (`llm`, `vision`, `tabular`), Pydantic istek şemaları (`InferenceRequest`, `ModelUpdate`), `Annotated` ile yol/sorgu parametresi kısıtlamaları (`Path`, `Query`), `dry_run` simülasyon mantığı ve Swagger UI (`/docs`) üzerinden doğrulanan `GET`, `POST`, `PUT` uç noktalarını içeren RESTful API uygulaması (`main.py`).
- **[`Task-And-Model-Hub-API/`](./Task-And-Model-Hub-API/)**: Kullanıcı kaydı ve yanıt filtreleme (`response_model=UserBase`, `response_model_exclude_unset=True`), iç içe görev şemaları (`TaskCreate`, `TaskUpdate`, `HttpUrl` ve `set[str]` içeren `EvidenceImage`), `openapi_examples` (`normal_gorev`, `kritik_ariza`), `dict[int, float]` ağırlık atama, `Body(embed=True)` ile `dry_run` güncelleme, `204 No Content` silme ve `/health-raw` uç noktalarını içeren FastAPI uygulaması (`main.py`).

### 🛠 Teknoloji Yığını ve Araçlar
- **Web Çatısı (Framework):** FastAPI (`APIRouter`/`app`, `Path`, `Body`, `Response`, `JSONResponse`, `status`)
- **Veri Doğrulama:** Pydantic v2 (`BaseModel`, `Field`, `EmailStr`, `HttpUrl`, `StrEnum`, `Annotated`)
- **ASGI Sunucusu:** Uvicorn
- **Programlama Dili:** Python 3.11+
- **Veri Saklama:** Bellek içi sözlükler (`dict`)
- **Versiyon Kontrolü:** Git, GitHub, GitHub Desktop