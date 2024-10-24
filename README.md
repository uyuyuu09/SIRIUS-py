# SIRIUS-py

SIRIUS-pyはPythonにより構築された、SIRIUSを運用するうえでセットアップする際に必要なシステムです。

## How to use?

コードをcloneし、必要な基礎データを所定のディレクトリに置き、src/main.pyを実行します。

```cmd
- SIRIUS-py
    - src
        - json
            member.json
        - main.py
    - .env
    - .gitignore
    - README.md
```

### member.jsonについて

このjsonファイルは、撮影対象者をリスト化したものです。以下のような構造を想定しています。

```cmd
{
    {
        "name": "IKEDA YUMA",
        "number": "3108",
        "memo": ""
    },
    {
        "name": "KBC ADMIN",
        "number": "3900",
        "memo": "撮影なし"
    }
}
```

> 各パラメータについて
>
> name : 氏名(必須)
>
> number : 学籍番号(教員の場合は9999, 必須)
>
> memo : 備考(任意)