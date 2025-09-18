# 8am AI Meetings Download Manifest

## Instructions

This manifest tracks all meetings with "8am" in the title for download processing. The table below contains:

- **Download Status**: Tracks the current state of each meeting's download process
  - `no` = Not yet downloaded
  - `in_progress` = Currently being processed  
  - `yes` = Successfully downloaded
  - `error` = Download failed (check notes)

- **Meeting ID**: Fireflies transcript ID used for API calls
- **Title**: Meeting title from Fireflies
- **Date**: Meeting date (YYYY-MM-DD format for folder naming)
- **Duration**: Meeting length in minutes
- **Files to Download**: 
  - Summary (from Fireflies summary.overview)
  - Transcript (using fireflies_get_transcript_details function)
  - Audio (direct download from audio_url)

## Important Notes

⚠️ **TRANSCRIPT EXTRACTION**: Use the `fireflies_get_transcript_details` function to get the actual TXT transcript content, NOT the HTML viewer URLs.

⚠️ **FOLDER STRUCTURE**: Create folders as `~/Desktop/8-am-ai/YYYY-MM-DD/` based on meeting date.

⚠️ **AUDIO URLS**: Audio URLs contain expiration timestamps - download immediately when processing.

## Download Tracking Table

| # | Status | Meeting ID | Title | Date | Duration | Folder Name | Notes |
|---|--------|------------|-------|------|----------|-------------|-------|
| 1 | yes | 01K2CYESYTN2NR7KDYWRGXV9J7 | 8am AI! | 2025-08-13 | 60.3 min | 2025-08-13 | Latest meeting |
| 2 | yes | 01K1TXNXAQ069V9A2S1E661TNW | 8am AI! | 2025-08-06 | 60.1 min | 2025-08-06 | - |
| 3 | yes | 01K18WWTW22CBZXV5B87SJK8N1 | 8am AI! | 2025-07-30 | 95.5 min | 2025-07-30 | Long meeting |
| 4 | yes | 01K0PW425JNMDSSVA4ZFW37212 | 8am AI! | 2025-07-23 | 62.3 min | 2025-07-23 | - |
| 5 | yes | 01K058QSS9T692YNNNGE8QNZVP | 8am-ai.com thinking chat 🤔 | 2025-07-18 | 51.2 min | 2025-07-18 | Different title format |
| 6 | yes | 01K04Z8ETDF5A7CDEGSN7DT1VS | 8am AI! | 2025-07-16 | 120.6 min | 2025-07-16 | Longest meeting |
| 7 | yes | 01JZ6DGP78CKVVF8Y4YY8M3GX3 | 8am AI! | 2025-07-09 | 50.3 min | 2025-07-09 | - |
| 8 | no | 01JZ0YAH1H2C4F3ZXP61S54RDG | 8am AI School | 2025-07-02 | 50.0 min | 2025-07-02 | School format |
| 9 | no | 01JYEXHZFMAE8HGNV90XDYSNN1 | 8am AI School | 2025-06-25 | 60.5 min | 2025-06-25 | School format |
| 10 | no | 01JXNR1ANXV3Z8RJ08YRATGG4A | 8am AI School | 2025-06-18 | 48.4 min | 2025-06-18 | School format |
| 11 | no | 01JXAVZPNTTC9QEDGV5RBW5HHJ | 8am AI School | 2025-06-11 | 62.1 min | 2025-06-11 | School format |
| 12 | no | 01JW6TDTFMN91TA3A78RAF3XYH | 8am AI School | 2025-05-28 | 10.8 min | 2025-05-28 | Short meeting |
| 13 | no | 01JVMSMZT77HJS2D2GB7VWY93W | 8am AI School | 2025-05-21 | 54.4 min | 2025-05-21 | School format |
| 14 | no | 01JV2RVQH36ENJXTVC0X7YR4A6 | 8am AI School | 2025-05-14 | 56.8 min | 2025-05-14 | School format |
| 15 | no | 01JTGR2E84W8V9AQYJ1V6X11A7 | 8am AI School | 2025-05-07 | 37.3 min | 2025-05-07 | School format |
| 16 | no | 01JSYQ9J1WC5ZRAESRC4YNBYMN | 8am AI School | 2025-04-30 | 60.7 min | 2025-04-30 | School format |
| 17 | no | 01JSCPG9S0PPMBDZFTYN7DZNRH | 8am AI School | 2025-04-23 | 65.8 min | 2025-04-23 | School format |
| 18 | no | 01JRTNQPF8FS11BSF8W7YXDJN8 | 8am AI School | 2025-04-16 | 50.3 min | 2025-04-16 | School format |
| 19 | no | 01JQPM56YW4DBA6GCH6VB2Y8YZ | 8am AI School | 2025-04-02 | 10.5 min | 2025-04-02 | Short meeting |
| 20 | no | 01JQ4KCARHZK66Z8998CA4MVMG | 8am AI School | 2025-03-26 | 71.2 min | 2025-03-26 | School format |
| 21 | no | 01JPJJKA5W3508779466SJGWJV | 8am AI School | 2025-03-19 | 63.0 min | 2025-03-19 | School format |
| 22 | no | 01JP0HT45YD95E0TBJZ4NZJWDD | 8am AI School | 2025-03-12 | 10.2 min | 2025-03-12 | Short meeting |
| 23 | no | 01JNEH16XFBJWVZNGW0P977WQ0 | 8am AI School | 2025-03-05 | 23.3 min | 2025-03-05 | Short meeting |
| 24 | no | 01JMWG84HTV9314PV0RAZZQE53 | 8am AI School | 2025-02-26 | 45.2 min | 2025-02-26 | School format |
| 25 | no | 01JMAFFGKCZFE0TWTJMT9P12ZC | 8am AI School | 2025-02-19 | 51.0 min | 2025-02-19 | School format |
| 26 | no | 01JKREP8SGJEMQ6SDBZ5AZ2CBF | 8am AI School | 2025-02-12 | 50.0 min | 2025-02-12 | School format |
| 27 | no | T91kKV2uubxIPbad | 8am AI School | 2025-02-05 | 59.0 min | 2025-02-05 | School format |
| 28 | no | FxQfUYmWEHXpf6dI | 8am AI School | 2025-01-29 | 79.0 min | 2025-01-29 | School format |
| 29 | no | oOdO04EdFGK5B9Nu | 8am AI School | 2025-01-22 | 47.0 min | 2025-01-22 | School format |
| 30 | no | AbDHyINiAP5LSXmj | 8am AI School | 2025-01-08 | 67.0 min | 2025-01-08 | School format |
| 31 | no | ZBJVCNeH7UUA6wQV | 8am AI School | 2025-01-01 | 10.0 min | 2025-01-01 | New Year meeting |
| 32 | no | S3EWNYz0oZdBzBv1 | 8am AI School | 2024-12-25 | 10.0 min | 2024-12-25 | Christmas meeting |
| 33 | no | W25gLxC6gEmyS3iG | 8am AI School | 2024-12-18 | 76.0 min | 2024-12-18 | School format |
| 34 | no | XKzxmdubXesUbex0 | 8am AI School | 2024-12-11 | 84.0 min | 2024-12-11 | School format |
| 35 | no | U4Ef14cwg7M5WT6y | 8am AI School | 2024-12-04 | 60.0 min | 2024-12-04 | School format |
| 36 | no | fP1Z24NTIJAg9a4l | 8am AI School | 2024-11-27 | 84.0 min | 2024-11-27 | School format |
| 37 | no | dscVmwG4O4lNAm2g | 8am AI School | 2024-11-20 | 64.0 min | 2024-11-20 | School format |
| 38 | no | 57nsqfI6s2hONywF | 8am AI School | 2024-11-13 | 77.0 min | 2024-11-13 | School format |
| 39 | no | GFSMOT0IVyhQm4MQ | 8am AI School | 2024-11-06 | 64.0 min | 2024-11-06 | School format |
| 40 | no | n9Vt361ZbpyOR9RS | 8am AI School | 2024-10-30 | 75.0 min | 2024-10-30 | School format |
| 41 | no | iJjFSYkLtmg8cBz9 | 8am AI School | 2024-10-23 | 84.0 min | 2024-10-23 | School format |
| 42 | no | Zbbzx1G4aAaeESA5 | 8am AI School | 2024-10-16 | 105.0 min | 2024-10-16 | Long meeting |
| 43 | no | 7ZGTPtCCusUFKrUJ | 8am AI School | 2024-10-09 | 57.0 min | 2024-10-09 | School format |
| 44 | no | bnv9miUKB1BHEIom | 8am AI School | 2024-10-02 | 89.0 min | 2024-10-02 | School format |
| 45 | no | yUS1H4315DYaGfBF | 8am AI School | 2024-09-25 | 79.0 min | 2024-09-25 | School format |
| 46 | no | 6yCNequ2dq07316z | 8am AI School | 2024-09-24 | 10.0 min | 2024-09-24 | Short meeting |
| 47 | no | nVDkUtii39f29CEj | 8am AI School | 2024-09-11 | 105.0 min | 2024-09-11 | Long meeting |
| 48 | no | VkrU8WTkUdETLjLr | 8am AI School | 2024-08-28 | 94.0 min | 2024-08-28 | School format |
| 49 | no | D3hxb2j2OZm3IKpg | 8am AI School | 2024-08-21 | 80.0 min | 2024-08-21 | School format |
| 50 | no | C0dZsXjG9Eis7aKA | 8am AI School | 2024-08-14 | 97.0 min | 2024-08-14 | School format |

## Download Commands Reference

### Get Summary
```bash
mcp__fireflies__get_summary --transcriptId="MEETING_ID" --filter='["summary { overview }"]'
```

### Get Transcript Text
```bash
fireflies_get_transcript_details --transcriptId="MEETING_ID"
```

### Download Audio
```bash
curl -o "audio.mp3" "AUDIO_URL_FROM_TABLE"
```

## Processing Workflow

1. Create folder: `mkdir -p ~/Desktop/8-am-ai/YYYY-MM-DD`
2. Update status to `in_progress` in this manifest
3. Get summary and save as `summary.txt`
4. Get transcript using `fireflies_get_transcript_details` and save as `transcript.txt`
5. Download audio as `audio.mp3`
6. Update status to `yes` when complete
7. Note any errors in the Notes column

---
**Total Meetings Found**: 50
**Download Progress**: 0/50 completed
**Last Updated**: 2025-08-13