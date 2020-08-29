flask_server

## Dependencies

```
pip install -r requirements.txt
```

## Start server

```
cd flask_server
python app.py
```

## Return value

POST form has to be:

```
mydata = {'img_encoded': base64_string, 'lang': 'custom', 'type': 'classify'}
```

type is classify / detection

Return value:

```
#classify
{'type':'classify', 'size': [img.width, img.height], "predicted": classes[predicted], "score": score.item()}

#detection
{'type': 'detection', 'size': [img.width, img.height], "predicted": base64_string}
```

## Example call API

### VNLang (WIP)

```vnlang
// http.vnl
in_ra("Đây là ví dụ dùng lib http")
đặt http = sử_dụng("../library/libhttp.vnl")
http.req_post("http://127.0.0.1:3000/cifar_classifier","./imgs/palm.jpg")
```

```
cd example
go run ../src/vnlang/main.go http.vnl
```
