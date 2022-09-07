from abc import ABCMeta, abstractmethod
import pandas as pd
import pickle

class AbstractInference(metaclass=ABCMeta):
    # モデルインスタンス
    __model = None

    # 説明変数データフレーム
    __df = None

    # 初期化
    def __init__(self,request):
        # モデルロード
        self.__model = pickle.load(open(self._model_file(), 'rb'))

        # リクエストパラメータを説明変数データフレーム変換
        df = self.__request_to_df(request)

        # 説明変数リネーム
        df = df.rename(columns=self.__x_colmuns(self._mapping()))

        # 保管
        self.__df = df

    # 推論タイトル
    # overrideしてタイトルをリターン
    @abstractmethod
    def _inference_title(cls):
        pass

    # マッピング辞書
    # overrideしてリターン
    @abstractmethod
    def _mapping(cls):
        pass

    # インプットタグ
    # overrideしてリターン
    @abstractmethod
    def _input(cls,k,v):
        pass

    # モデルファイル
    # overrideしてリターン
    @abstractmethod
    def _model_file(self):
        pass

    # 結果表示文字列
    # overrideしてリターン
    @abstractmethod
    def _result_to_string(self,y):
        pass

    # リクエストパラメータを説明変数データフレーム変換
    def __request_to_df(self,request):
        values = []
        for k in self._mapping():
            values.append(request.form[k])
        
        return pd.DataFrame([values])

    # 予測
    def __predicting(self,X):
        return self.__model.predict(X)

    # 説明変数及びFORMマッピング辞書を説明変数のリネーム辞書に変換
    def __x_colmuns(self,d):
        i = 0
        dict = {}
        for k in self._mapping():
            dict[i] = k
            i += 1
        return dict

    # 正規化及び標準化
    def _scaling(self,X):
        return X

    # 実行メソッド
    def __execute(self):
        self.__df = self._scaling(self.__df)
        # 予測を実行
        result_y = self.__predicting(self.__df)
        # 結果を整形して返す
        return self._result_to_string(result_y)
        
    # index.htmlへの説明変数入力Form
    @classmethod
    def form(cls):
        form = """
        <div class="offset-2 col-8 text-center mt-4 mb-2">{title}</div>
        """.format(title=cls._inference_title())
        for k in cls._mapping():
            input = cls._input(k,cls._mapping()[k])
            form = form + cls.__form_builder(input)

        return form
    
    # 各説明変数FormInputタグパーツ生成
    @classmethod
    def __form_builder(cls,input):
        return input

    # 外部からの呼び出しメソッド
    @classmethod
    def drive(cls,inference):
        
        return inference.__execute()

