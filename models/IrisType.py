from models.AbstractInference import AbstractInference

# アヤメの品種分類
class IrisType(AbstractInference):

    # タイトル
    @classmethod
    def _inference_title(cls):
        return "アヤメ品種推論"

    # マッピング辞書
    @classmethod
    def _mapping(cls):
        return {
            'SEPAL_LENGTH':'萼片長(cm)',
            'SEPAL_WIDTH':'萼片幅(cm)',
            'PETAL_LENGTH':'花弁長(cm)',
            'PETAL_WIDTH':'花弁幅(cm)'
        }

    # インプットタグ
    @classmethod
    def _input(cls,k,v):
        return '''
        <div class="offset-2 mt-3 col-8">
        <label class="form-label" for="{key}">{val}</label>
        <input type="number" step="0.1" class="form-control mb-0" id={key} name="{key}" placeholder="{key}" required>
        </div>
        '''.format(key=k,val=v)

    # 説明変数及びFORMマッピング辞書
    def _model_file(self):
        return 'saves/iris_RandomForestClassifier_model.sav'
 
    # 結果表示文字列
    def _result_to_string(self,y):
        iris_type = ['setosa','versicolor','virginica']
        return "アヤメの品種は {} です。".format(iris_type[y[0]])

if __name__ == "__main__":
    exit()
