## Pytest Decorators

### @pytest.mark.parametrize

`@pytest.mark.parametrize` dekoratörü, bir testi farklı argümanlarla birden çok kez çalıştırmak için kullanılır. İki
parametre alır: 1. parametre fonksiyonun adı, 2. parametre fonksiyon için değerlerin listesi. Listedinin her değeri için
bir kez çalıştırılacaktır.

```python
@pytest.mark.parametrize("test_fn", ["value1", "value2"])
def test_fn(test_fn):
    ...
```

### @pytest.mark.skip

`@pytest.mark.skip` dekoratörü, bir testi çalıştırmadan atlamak için kullanılır. `reason` parametresi ile neden
atlandığını belirtmek için kullanılabilir.

```python
@pytest.mark.skip(reason="not implemented yet")
def test_fn():
    ...
```

### @pytest.mark.xfail

`@pytest.mark.xfail` dekoratörü, bir testin beklenen bir şekilde başarısız olacağını belirtmek için kullanılır.

```python
@pytest.mark.xfail
def test_fn():
    ...
```

### @pytest.mark.usefixtures

`@pytest.mark.usefixtures` dekoratörü, bir testin başka bir testin fixture'lerini kullanmasını sağlar.

```python
@pytest.fixture
def fixture1():
    ...


@pytest.fixture
def fixture2():
    ...


@pytest.mark.usefixtures("fixture1", "fixture2")
def test_fn():
    ...
```

### @pytest.mark.filterwarnings

`@pytest.mark.filterwarnings` dekoratörü, bir testin belirli bir uyarıyı göstermemesini sağlar.

```python
@pytest.mark.filterwarnings("ignore::DeprecationWarning")
def test_fn():
    ...
```

### @pytest.mark.skipif

`@pytest.mark.skipif` dekoratörü, bir testin belirli bir koşula göre çalıştırılmasını sağlar. 1. parametre koşul, 2.
parametre neden olarak kullanılır.

```python
@pytest.mark.skipif(condition, reason="reason")
def test_fn():
    ...
```

### @pytest.mark.timeout

`@pytest.mark.timeout` dekoratörü, bir testin belirli bir süre içinde bitmesini sağlar.

```python
@pytest.mark.timeout(1)
def test_fn():
    ...
```

### @pytest.mark.asyncio

`@pytest.mark.asyncio` dekoratörü, bir testin asenkron bir şekilde çalıştırılmasını sağlar.

```python
@pytest.mark.asyncio
async def test_fn():
    ...
```

### @pytest.mark.freeze_time

`@pytest.mark.freeze_time` dekoratörü, bir testin belirli bir tarihe sahip olduğunu simüle eder.

```python
@pytest.mark.freeze_time("2020-01-01")
def test_fn():
    ...
```
