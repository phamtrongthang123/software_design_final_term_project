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



## Example call API 

### VNLang 

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

