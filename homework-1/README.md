# Ödev - 1

## Python Veri Yapıları

### Metinsel Veri Tipleri

`string` : Metinsel veri tiplerini ifade eder.

**Örnek** :

```python
name = "Python"
```

### Sayısal Veri Tipleri

`integer` : Tam sayısal veri tiplerini ifade eder.

**Örnek** :

```python
age = 25
```

`float` : Ondalıklı sayısal veri tiplerini ifade eder.

**Örnek** :

```python
height = 1.75
```

`complex` : Karmaşık sayısal veri tiplerini ifade eder. (İmajiner sayılar) "j" ile ifade edilir.

**Örnek** :

```python
complex_number = 3 + 5j
```

### Mantıksal Veri Tipleri

`boolean` : Mantıksal veri tiplerini ifade eder. (True - False)

**Örnek** :

```python
is_student = True
```

### Diziler

`list` : Dizileri ifade eder. (Sıralı, Değiştirilebilir, farklı tip veri tutabilir)

**Örnek** :

```python
myList = [1, 2, 3, 4, "Python"]
```

`tuple` : Dizileri ifade eder. (Sıralı, Değiştirilemez, farklı tip veri tutabilir)

**Örnek** :

```python
myTuple = (1, 2, 3, 4, "Python")
```

`range` : Dizileri ifade eder. (Sıralı, Değiştirilemez, sadece sayısal veri tutabilir)

**Örnek** :

```python
myRange = range(1, 10)
```

### Sözlük

`dictionary` : Sözlükleri ifade eder. Verilen anahtar değerine göre veriye erişim sağlanır.

**Örnek** :

```python
myDictionary = {
    "name": "John",
    "age": 25,
    "height": 1.75,
    "is_student": True
}
```

### Küme

`set` : Kümelere ifade eder. (tekrar eden verileri içermez, değiştirilebilir, sırasız olduğu için indeksleme yapılamaz)

**Örnek** :

```python
mySet = {1, 2, 3, 4, "Python"}
```

`frozenset` : Kümelere ifade eder. Değiştirilemez bir set oluşturmak için kullanılır. (tekrar eden verileri içermez,
değiştirilemez, sırasız olduğu için indeksleme yapılamaz)

**Örnek** :

```python
myFrozenSet = frozenset({1, 2, 3, 4, "Python"})
```

### Binary Veri Tipleri

`bytes` : Binary veri tiplerini ifade eder. Her bir karakterin 1 byte yer kapladığı veri tipidir.

**Örnek** :

```python
myBytes = b"Python"
```

`bytearray` : Binary veri tiplerini ifade eder. Byte veri tipinde oluşturulan verileri değiştirmek için kullanılır.

**Örnek** :

```python
myByteArray = bytearray(5)
```

`memoryview` : Binary veri tiplerini ifade eder. Bellekteki verileri görüntülemek için kullanılır.

**Örnek** :

```python
myMemoryView = memoryview(bytes(5))
```

## Kodlama.io sitesindeki veri tipleri

`string` : Navigasyon, kurs adı, kurs açıklaması, kursun eğitmeni, kursun tarihi

`integer` : Tamamlanma oranı, toplam yorum sayısı

`list` : Kursun eğitmenleri, kursun kategorileri, kursların içeriği, yorumlar

`boolean` : Bölümün tamamlanıp tamamlanmadığı

## Kodlama.io sitesindeki şart blokları

`if` : Eğer o anki bölüm tamamlanmışsa bölümü tamamlanmış olarak işaretleyip bir sonraki bölüme geçer.

```python
is_completed = True
checkBox = "unchecked"

if is_completed:
    checkBox = "checked"
else:
    checkBox = "unchecked"
```