
# GOVCOPP Publications Dataset (2020–2026)

This dataset brings together publications associated with **GOVCOPP researchers** for the period **2020–2026**, based on the records contained in the supplied files.

The dataset is organised into three complementary files, allowing users to work separately with **authorship**, **publications**, or an **integrated version** combining both dimensions.

## Files

### 1. `authorship_2020_2026.csv`
**Authorship / researcher identification file**

Long-format structure: each row represents the relationship between one publication and one GOVCOPP researcher.

Fields:
- `publication_id` — unique publication identifier;
- `researcher_id` — researcher identifier, in the format `Rxxx`;
- `source` — source of the record;
- `formal_group` — GOVCOPP formal group associated with the researcher;
- `category` — researcher category (`integrado` or `colaborador`).

File size:
- **4,363 publication–researcher relationships**;
- **3,343 distinct publications**;
- **187 distinct researchers**.

This is the most appropriate file for analyses of:
- authorship and co-authorship;
- collaboration networks;
- publication output by researcher;
- publication output by GOVCOPP group;
- linking publications to researchers.

> Note: this file does not contain researcher names; it uses researcher identifiers only.

---

### 2. `publications_2020_2026.csv`
**Publications file**

Each row corresponds to **one publication**.

File size:
- **3,343 publications**;
- **36 variables**;
- publication years from **2020 to 2026**.

It includes, among others:
- bibliographic identifiers (`publication_id`, `eid`, `scopus_id`, `doi`);
- publication year, title and abstract;
- source title and source type;
- document type;
- citation count;
- journal/source information;
- ISSN/eISSN;
- publisher;
- subject areas;
- available bibliometric indicators, including CiteScore, SJR and SNIP, together with their reference years;
- derived document classification variables;
- number of GOVCOPP researchers associated with the publication (`govcopp_researcher_count`);
- GOVCOPP groups represented in the publication (`govcopp_groups`).

This is the most appropriate file for:
- bibliometric analysis;
- analysis of publication trends over time;
- title and abstract analysis;
- analysis by publication or source type;
- subject-area analysis;
- analysis of impact and journal/source indicators.

---

### 3. `publications_authors_2020_2026.csv`
**Integrated file: publications + researchers**

Each row corresponds to **one publication**, combining bibliographic metadata with the GOVCOPP researchers associated with it.

File size:
- **3,343 publications**;
- **58 variables**.

In addition to the variables contained in `publications_2020_2026.csv`, it includes:
- `govcopp_authors` — set of GOVCOPP researcher identifiers associated with the publication;
- `govcopp_author_1` ... `govcopp_author_7` — individual researcher identifiers associated with the publication;
- for each researcher, the corresponding:
  - `formal_group`;
  - `category`.

This file is particularly useful when the objective is to work with **a single table** combining bibliographic and authorship information.

> For network analysis, co-authorship analysis, or other many-to-many relationships, `authorship_2020_2026.csv` is preferable because its structure is better suited to this type of analysis.

---

## Relationship between the files

The common variable is:

`publication_id`

The logical structure can be represented as:

```text
publications_2020_2026.csv
        1
        |
        | publication_id
        |
        N
authorship_2020_2026.csv
```

A publication may be associated with one or more GOVCOPP researchers.

`publications_authors_2020_2026.csv` is an integrated version of this information, keeping one row per publication and distributing researchers across multiple columns.

---

## Corpus summary

| Indicator | Value |
|---|---:|
| Period covered | 2020–2026 |
| Distinct publications | 3,343 |
| Distinct researchers | 187 |
| Publication–researcher relationships | 4,363 |
| Source indicated in the authorship file | Scopus |
| Researcher categories | integrado; colaborador |
| Formal groups represented | CIS; TD; SAD; PI2 |

### Documented group correction

On 2026-10-19, the four authorship rows for researcher `R093` were corrected from `PI3` to `PI2`. The corresponding `govcopp_groups` fields in `publications_2020_2026.csv` and both the group and author-group fields in the optional integrated file were corrected for the same four publications. The two files used for W06 now match the corrected teaching files byte for byte. Publication and researcher identifiers, titles, and authorship links did not change.

| File | SHA-256 before correction | SHA-256 after correction |
|---|---|---|
| `authorship_2020_2026.csv` | `512f30215fe028935fc599667a6632e017f99f6d9f77f2892258e7f555c66338` | `41a9e5fbc512d3d7e015e4d0dc7beed6daa3d2d15049e94bab90d582d3604d73` |
| `publications_2020_2026.csv` | `badca2d7219a3f5b14a2c9f6f7b100a4c094ffe0dcbe6431a966a0471c3b7362` | `60b1ab3f6ce49d7edcb65506f5adffb9c3f279f3ea1065e4240b3744a87961be` |
| `publications_authors_2020_2026.csv` | `526c9e6e3b3861f14ecaa6528a0eca5baf2c129c252b136df0b2f5dc2dbe538c` | `ca6b83deaaee435ea329e882897c9bdbc157f5cf05d512c5d9ef48da2c363b8d` |

---

## File formats

- `authorship_2020_2026.csv` — comma-separated;
- `publications_2020_2026.csv` — comma-separated;
- `publications_authors_2020_2026.csv` — semicolon-separated (`;`) and includes a first line `sep=;`, to facilitate opening in applications such as Microsoft Excel.

All files use `publication_id` as the publication identifier.

---

## Interpretation notes

1. **Unit of analysis**  
   In the publication files, the unit of analysis is the publication. In the authorship file, the unit of analysis is the publication–researcher relationship.

2. **Publication counts by researcher**  
   These should preferably be calculated from `authorship_2020_2026.csv`.

3. **GOVCOPP co-authorship**  
   A publication with several GOVCOPP researchers generates several rows in `authorship_2020_2026.csv`, but only one row in the two publication-level files.

4. **Bibliometric indicators**  
   CiteScore, SJR, SNIP and citation counts should be interpreted as values available at the time of data extraction. Source-level indicators include the reference year where available.

5. **Missing values**  
   Some bibliographic fields and indicators may not be available for all publications or source types.

6. **Year 2026**  
   The dataset includes publications from 2026. Completeness for that year depends on the date of data extraction and should not be assumed without that information.

---

## Recommended use

- **Who published what?** → `authorship_2020_2026.csv`
- **What publications are included and what are their characteristics?** → `publications_2020_2026.csv`
- **I want all information in a single table** → `publications_authors_2020_2026.csv`
