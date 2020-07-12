# ckkw
# カタカナ綴りのブレを減らしましょう

ckkw はこれまで日本語に翻訳した技術的文章で使われたカタカナを集めたものを使い、利用者が新たに作成した日本語の技術文章を読み、
使われているカタカナが既存のデータに含まれていないものを表示します。
多くの場合は、英単語で２つのワードであったものを無意識の内に１ワードのカタカナにしているものなどがあります。

例：エラーメッセージ：これは英文では error message であったものなので　「エラー メッセージ」のように半角のスペースを入れると読みやすくなります。
例外として：オープンソースは 英文では open source ですが、日本語でも１ワードで使われることが多いため１ワードでも良しとしています。

# 機能

- 指定されたテキスト ファイルを読み、既に持っているカタカナ データと比較し、登録されていないものをリストします。
- 登録されていないカタカナが見つかった行番号と共にオリジナル テキストを表示してどこに存在したかを示します。
- unknown.txt という名前で、登録されていなかったカタカナを１行に１ワードのテキスト ファイルで出力します。
このファイルを見ることで、新たに登録すべき単語を取り出し、addkkw コマンドでカタカナ データを追加することができます。カタカナ データは kkw.txt として集めていますが、今後このファイルは別なライセンスで公開する予定です。

# インストール

`$ mkdir myckkw; cd myckkw`      # 適切なディレクトリを用意し、移動します。

`$ git clone github.com/tgkz/ckkw.git`

`$ python3 setup.py install [--user]`

                      現状では --user の利用を推奨します。

# 使い方


`$ export KKWPATH=<kkw.txtが存在するディレクトリ> `

現状では data の下に kkw.txt がありますので、myckkw/data/ とすれば良いでしょう。

`$ ckkw <テキスト ファイル>`

ckkw 単体ではテキスト ファイルからしか読めませんが、ckkkw.sh を利用すれば
http, docx, odt, pdf などからテキストに変換して ckkw に渡すことができます。

オフィスで作成したファイル mydoc.docx から読み込みます。

`$ ckkkw.sh <mydoc.docx>`

http://www.aaa.bbb.com に公開されている html のドキュメントから読み込みます。

`$ ckkkw.sh http://www.aaa.bbb.com`


# コントリビューション

[issue tracker](https://github.com/tgkz/ckkw/issues) を使って皆さんの問題や機能リクエストをお送りください。

また、カタカナのデータの追加についてもリクエストください。


