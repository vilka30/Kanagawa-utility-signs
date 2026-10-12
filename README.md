# Таблички на столбах Канагавы

База табличек по надписям на опорах линий связи в префектуре Канагава, Япония.

Проект посвящён сбору надписей на табличках и описанию их ареала.

## Языки

Исходные версии файлов написаны на русском языке.

Английские версии добавляются постепенно.
## Проверки
В репозитории находятся небольшие Python-скрипты для проверки и статистики базы:

scripts/
- poles_counter.py
- repeat_checker.py
- spelling_checker.py
- mark_counter.py

Они используются для подсчёта записей, поиска повторов, проверки формата некоторых надписей и подсчёта оценок при наличии.

После завершения работы над населённым пунктом он переходит в стадию проверки, которая длится примерно несколько месяцев. В этот период проводится проверка случайной выборки надписей, поиск табличек в GeoGuessr с использованием только табличек, а также просмотр Google Maps для проверки уже внесённых данных и поиска новых табличек.

## Примечание

Стоит учесть, что здесь, вероятно, не охвачены все существующие таблички. Кроме того, некоторые области, где может встретиться надпись, определены по собственным наблюдениям и могут содержать неточности или ошибки.

## Источники

- https://geoshape.ex.nii.ac.jp
- https://google.com/maps


# Kanagawa Utility Pole Signs

A database of signs found on utility poles carrying telecommunications lines in Kanagawa Prefecture, Japan.

The project focuses on collecting inscriptions on signs and documenting their distribution area.

## Languages

The original versions of the files are written in Russian.

English versions are being added gradually.

## Checks

The repository contains small Python scripts for checking and maintaining statistics for the database:

scripts/
- poles_counter.py
- repeat_checker.py
- spelling_checker.py
- mark_counter.py

They are used to count entries, find duplicates, check the format of some labels, and count ratings when available.

After work on a settlement is completed, it enters a review stage that lasts several months. During this period, a random sample of inscriptions is checked, signs are searched for in GeoGuessr using only signs as clues, and Google Maps is browsed to verify existing data and find new signs.

## Note

Please keep in mind that this database probably does not cover all existing signs. In addition, some areas where a particular sign may be found have been determined based on personal observations and may contain inaccuracies or errors.

## Sources

- https://geoshape.ex.nii.ac.jp
- https://google.com/maps


# 神奈川県の電柱標識

日本・神奈川県の通信線の電柱に取り付けられている標識をまとめたデータベースです。

このプロジェクトでは、標識に記された文字や名称を収集・記録し、その分布域を明らかにすることを目的としています。

## 言語

ファイルの原版はロシア語で作成されています。

英語版は順次追加しています。

## チェック

リポジトリには、データベースの確認や集計を行うための小さな Python スクリプトがあります。

scripts/
- poles_counter.py
- repeat_checker.py
- spelling_checker.py
- mark_counter.py

これらは、登録数の集計、重複の確認、一部の標識の表記形式の確認、評価がある場合の評価数の集計などに使用しています。

ある市町村の作業が完了すると、確認段階に移行します。この段階は数か月間続きます。その間、標識の記録をランダムに抽出して確認するほか、標識のみを手がかりにGeoGuessrで標識を探したり、Google マップを閲覧して登録済みのデータを確認し、新たな標識を探したりします。

## 注意

このデータベースには、存在するすべての標識が収録されているとは限りません。

また、特定の標識が見つかる可能性のある地域の一部は、個人的な観察に基づいて判断しています。そのため、不正確な情報や誤りが含まれている可能性があります。

## 情報源

- https://geoshape.ex.nii.ac.jp
- https://google.com/maps
