# 🚀 FastAPI Practices & Model Schemas

<p align="center">
  <a href="#english">English</a> | <a href="#türkçe">Türkçe</a>
</p>

---

## <a id="english"></a>🇬🇧 English

This module contains structured FastAPI exercises, request validation practices, and RESTful API endpoint patterns built with Python and Pydantic, focused on developing robust backend service skills.

### 📂 Repository Structure

* **`Model-Schemas-And-Endpoints/`**: RESTful API implementation (`main.py`) featuring `StrEnum` model family routing (`llm`, `vision`, `tabular`), Pydantic request schemas (`InferenceRequest`, `ModelUpdate`), `Annotated` path/query parameter constraints (`Path`, `Query`), `dry_run` update simulation logic, and Swagger UI (`/docs`) verification overview (`docs-overview.png`).

  ![FastAPI Swagger Overview](./docs-overview.png)

### 📝 Project Solutions & Evaluation Guide

Below is the structured overview of the practical FastAPI tasks completed in this section, along with technical assessments:

1. **Enum Routing & Pydantic Schema Definitions (`ModelFamily`, `InferenceRequest`, `ModelUpdate`)**
   * **Status:** Excellent. Successfully defined `ModelFamily(StrEnum)` to restrict valid model family values (`llm`, `vision`, `tabular`). Designed `InferenceRequest` (`prompt`, default `max_tokens=256`, optional `tags`) and `ModelUpdate` (`name`, nullable `description`, `temperature`, default `active=True`) using modern Python type annotations (`str | None`).

2. **Model Retrieval & Query Parameter Constraints (`GET /models/{family}`)**
   * **Status:** Fully Correct. Accurately implemented path validation via `ModelFamily` alongside `Annotated` query constraints: `top_k` bounded between `1` and `50` (`Query(ge=1, le=50)`) and hyphenated query parameter aliasing (`Query(alias="model-label")`) mapped cleanly to `labels`.

3. **Request Body Validation & Simulated Inference (`POST /models/{family}/predict`)**
   * **Status:** Outstanding. Implemented typed JSON body parsing via `InferenceRequest`, converted incoming models to standard Python dictionaries using `.model_dump()`, and returned structured responses containing `family`, `prediction_id`, the serialized request payload, and a simulated model output preview.

4. **Path Constraints & Dry-Run Update Pattern (`PUT /models/{model_id}`)**
   * **Status:** Flawless. Enforced positive integer validation (`gt=0`) on `model_id` using `Annotated[int, Path(gt=0)]`, paired with `ModelUpdate` request body validation and an optional `dry_run: bool = False` query flag to safely preview updates before persistence.

### 🛠 Tech Stack & Tools

* **Web Framework:** FastAPI
* **Data Validation:** Pydantic (`BaseModel`, `StrEnum`, `Annotated`)
* **ASGI Server:** Uvicorn
* **Language:** Python 3.11+
* **Version Control:** Git, GitHub

---

## <a id="türkçe"></a>🇹🇷 Türkçe

Bu modül, Python ve Pydantic kullanılarak geliştirilmiş yapılandırılmış FastAPI egzersizleri, istek doğrulama (request validation) pratikleri ve RESTful API uç nokta desenlerini içermekte olup, sağlam backend servis becerileri geliştirmeyi amaçlamaktadır.

### 📂 Depo Yapısı

* **`Model-Schemas-And-Endpoints/`**: `StrEnum` tabanlı model ailesi yönlendirmesi (`llm`, `vision`, `tabular`), Pydantic istek şemaları (`InferenceRequest`, `ModelUpdate`), `Annotated` ile yol/sorgu parametresi kısıtlamaları (`Path`, `Query`), `dry_run` güncelleme simülasyon mantığı ve Swagger UI (`/docs`) doğrulama ekran görüntüsünü (`docs-overview.png`) içeren RESTful API uygulaması (`main.py`).

  ![FastAPI Swagger Genel Görünümü](./docs-overview.png)

### 📝 Proje Çözümleri ve Değerlendirme Rehberi

Bu bölümde tamamlanan pratik FastAPI görevlerinin yapılandırılmış özeti ve teknik değerlendirmeleri aşağıdadır:

1. **Enum Yönlendirmesi ve Pydantic Şema Tanımları (`ModelFamily`, `InferenceRequest`, `ModelUpdate`)**
   * **Durum:** Mükemmel. Geçerli model ailesi değerlerini (`llm`, `vision`, `tabular`) sınırlandırmak için `ModelFamily(StrEnum)` tanımlandı. Modern Python tip bildirimleri (`str | None`) kullanılarak `InferenceRequest` (`prompt`, varsayılan `max_tokens=256`, isteğe bağlı `tags`) ve `ModelUpdate` (`name`, boş geçilebilir `description`, `temperature`, varsayılan `active=True`) şemaları oluşturuldu.

2. **Model Listeleme ve Sorgu Parametresi Kısıtlamaları (`GET /models/{family}`)**
   * **Durum:** Tamamen Doğru. `ModelFamily` üzerinden yol doğrulaması ile birlikte `Annotated` sorgu kısıtlamaları eksiksiz uygulandı: `top_k` parametresi `1` ile `50` arasında sınırlandırıldı (`Query(ge=1, le=50)`) ve URL'de tireli kullanım için `Query(alias="model-label")` takma adı `labels` parametresine eşlendi.

3. **İstek Gövdesi Doğrulama ve Simüle Edilmiş Tahmin (`POST /models/{family}/predict`)**
   * **Durum:** Harika. `InferenceRequest` ile tipli JSON gövde ayrıştırma uygulandı, gelen modeller `.model_dump()` ile standart Python sözlüklerine dönüştürüldü ve `family`, `prediction_id`, serileştirilmiş istek gövdesi ile simüle edilmiş model çıktı önizlemesini içeren yapılandırılmış yanıtlar döndürüldü.

4. **Yol Kısıtlamaları ve Dry-Run Güncelleme Deseni (`PUT /models/{model_id}`)**
   * **Durum:** Kusursuz. `Annotated[int, Path(gt=0)]` kullanılarak `model_id` değerinin `0`'dan büyük bir tam sayı olması zorunlu kılındı; `ModelUpdate` istek gövdesi doğrulaması ve kalıcı kayıt öncesinde güncellemeleri güvenle önizlemek için isteğe bağlı `dry_run: bool = False` sorgu parametresi eklendi.

### 🛠 Teknoloji Yığını ve Araçlar

* **Web Çatısı (Framework):** FastAPI
* **Veri Doğrulama:** Pydantic (`BaseModel`, `StrEnum`, `Annotated`)
* **ASGI Sunucusu:** Uvicorn
* **Programlama Dili:** Python 3.11+
* **Versiyon Kontrolü:** Git, GitHub

---