> 🇧🇷 [Portuguese version](README.pt.md)

# Cum‑Separated Values: The Alt‑Right and the Semen Retention Movement

This repository contains the corpus, IRaMuTeQ report, and data‑processing script used for the expanded abstract “Cum‑Separated Values: The Alt‑Right and the Semen Retention Movement” by Robert de Amorim Pontes and Victor Gabriel de Almeida Pedra.

## About the study

The study proposes the psychoanalytic metaphor of **Cum‑Separated Values** to examine how the datafication of bodily _jouissance_ mirrors obsessive‑neurotic strategies of control and resonates with the identity‑purity discourse of the alt‑right.

The hypothesis is that there is a structural homology between the psychic economy of the digital semen‑retention movement and the identity‑purity discourse that fuels the alt‑right. The article does not assert a direct political affiliation of community members; rather, it points to a shared logic of separation and control: the same comma that separates data in a `*.csv` file is used to separate and manage bodily energy, and this logic echoes the border‑policing rhetoric of far‑right movements.

## How the data support the hypothesis

The IRaMuTeQ analysis (Reinert / CHD method) partitioned the discourse into four classes. The two main classes reveal the core structure:

- **Class 3 — External Threat and Vital Capital (84.7% of segments):** Dominated by terms such as _woman_, _energy_, _power_, _life_, _sperm_, and _addiction_. This class portrays a worldview under siege, in which the feminine, pornography, and any form of “leakage” threaten the male vital essence.

- **Class 4 — Biological Metrics (14.5%):** Strongly characterised by _testosterone_, _test_, _level_, _increase_, _lab_, _diet_, and _streak_. It reflects an obsession with quantifying, monitoring, and optimising the body — a veritable “spreadsheet of the self” that attempts to render _jouissance_ manageable.

The high classification rate (94.9% of segments retained) indicates a highly cohesive, repetitive lexicon, consistent with a community structured around dogmatic, self‑referential discourse. The similarity graph confirms that temporal terms (_day_, _streak_, _time_) form the backbone of stability, while _woman_ and _addiction_ appear as agents of systemic instability.

These findings provide lexical evidence for the Cum‑Separated Values metaphor: the corpus is organised around delimiting what is inside (accumulated energy, metrics, discipline) and what is outside (women, pornography, loss). The homology with alt‑right discourse is drawn theoretically — supported by the references cited in the article — rather than through direct user overlap or cross‑community analysis, which lies beyond the scope of an expanded abstract.

## Repository contents

| Path | Description |
|------|-------------|
| `main.py` | Python script for cleaning and compiling the Reddit thread exports. |
| `jsons/` | Raw JSON exports of the 10 most‑engaged r/Semenretention threads. |
| `corpus_iramuteq.txt` | Final textual corpus formatted for IRaMuTeQ. |
| `RAPPORT.txt` | IRaMuTeQ lexical analysis report (Reinert / CHD method). |
| `README.md` | This file (English version). |
| `README.pt.md` | Portuguese version of this readme. |

## How the data were obtained

1. **Selection**: The 10 “Top All Time” threads from **r/Semenretention** were identified (accessed May 2026). The selected and used threads were:
   - [Thread 1](https://www.reddit.com/r/Semenretention/comments/m1eo4u/the_modern_struggle/)
   - [Thread 2](https://www.reddit.com/r/Semenretention/comments/frvg29/semen_retention_the_good_the_bad_and_the_ugly/)
   - [Thread 3](https://www.reddit.com/r/Semenretention/comments/mme87s/cultivating_a_high_sexual_charge/)
   - [Thread 4](https://www.reddit.com/r/Semenretention/comments/nocbbe/female_attraction_explained/)
   - [Thread 5](https://www.reddit.com/r/Semenretention/comments/wsu60w/300_day_semen_retention_streak_free_testosterone/)
   - [Thread 6](https://www.reddit.com/r/Semenretention/comments/n0dcmi/nikola_teslas_attitude_on_sex_1935/)
   - [Thread 7](https://www.reddit.com/r/Semenretention/comments/hod39f/why_the_elites_want_you_to_keep_ejaculating/)
   - [Thread 8](https://www.reddit.com/r/Semenretention/comments/jcxr46/mike_tysons_own_words_on_sex/)
   - [Thread 9](https://www.reddit.com/r/Semenretention/comments/lux0jo/on_a_good_streak_cannot_sit_still_overload_of/)
   - [Thread 10](https://www.reddit.com/r/Semenretention/comments/l23ire/a_quick_and_easy_explanation_for_the_benefits_of/)

2. **Download**: Each thread (original post + all nested comments) was exported as a single JSON file using the free tool [Reddinbox Download Reddit Thread](https://reddinbox.com/free-tools/download-reddit-thread).  
   - Paste the thread URL → click **Download** → save the `*.json` file.  
   - Repeat for all threads.
3. The resulting JSON files are located in the `jsons/` folder of this repository.

## Environment and execution

The script requires **Python 3.12** and uses only the standard library (`json`, `re`, `os`).  
We recommend managing the environment with [**uv**](https://docs.astral.sh/uv/).

### Setup with uv

```bash
# Install uv if necessary: https://docs.astral.sh/uv/
uv python install 3.12           # ensure Python 3.12 is available
```

Then execute the script:

```bash
uv run python main.py
```

The script reads all `*.json` files from the `jsons/` folder and generates `corpus_iramuteq.txt`.
During execution, it prints the number of processed files and text segments.

## IRaMuTeQ analysis details

The corpus was analysed with [IRaMuTeQ (v0.8 alpha 7)](https://pratinaud.gitpages.huma-num.fr/iramuteq-website/) using the following parameters:

- **Segment size (ST):** ~20 words.
- **Lemmatisation:** native English dictionary.
- **Minimum class size for CHD:** 13 text segments.
- **Visualisations:** dendrogram and similarity graph (omitted from the article due to page limits and restrictions on the use of images and/or tables, but available in the software’s interactive output).

The complete statistical report is available in `RAPPORT.txt`. It includes:

- Chi‑squared (χ²) values for each term per class.
- Class sizes and proportions.
- Full term lists with contributions.

The expanded abstract discusses only the two dominant classes (3 and 4) because the other two (1 and 2) contained about 0.7% of segments and were residual (nutritional vocabulary, book recommendations).

## How to cite this repository

When using this dataset or code, please cite it as:

> Pontes, Robert de Amorim; Pedra, Victor Gabriel de Almeida. **Cum‑Separated Values: The alt‑right and the semen retention movement** [Data set and code]. Zenodo. DOI: XXXXXXX. Available at: <https://doi.org/XXXXXXX>.

## Licence

This work is licensed under the Creative Commons Attribution‑NonCommercial‑ShareAlike 4.0 International License. To view a copy of this license, visit [http://creativecommons.org/licenses/by-nc-sa/4.0/](http://creativecommons.org/licenses/by-nc-sa/4.0/).

## Contact

Questions? Open an issue in this repository or contact the authors.
