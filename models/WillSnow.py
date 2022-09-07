from models.AbstractInference import AbstractInference
from sklearn.preprocessing import StandardScaler
import pickle

# アヤメの品種分類
class WillSnow(AbstractInference):

    # タイトル
    @classmethod
    def _inference_title(cls):
        return "山形県新庄市降雪についての推論"

    # マッピング辞書
    @classmethod
    def _mapping(cls):
        return {
            'HIGH':'最高気温(℃)',
            'LOW':'最低気温(℃)',
            'DAYLIGHT_HOURS':'日照時間(時間)',
            'AVG_PRESSURE':'平均現地気圧(hPa)'
        }

    # インプットタグ
    @classmethod
    def _input(cls,k,v):
        return '''
        
        <div class="col-6 my-2">
        <label class="form-label" for="{key}">{val}</label>
        <input type="text" class="form-control" id={key} name="{key}" placeholder="{key}" required>
        </div>
        '''.format(key=k,val=v)

    # 説明変数及びFORMマッピング辞書
    def _model_file(self):
        return 'saves/yamagataken_shinjoshi_snow_RandomForestClassifier_model.sav'
 
    # 結果表示文字列
    def _result_to_string(self,y):
        snow = ['雪が降りません','雪が降ります']
        return "入力値の翌日は {} ".format(snow[y[0]])

    # 正規化及び標準化
    def _scaling(self,X):
        return X

if __name__ == "__main__":
    exit()
