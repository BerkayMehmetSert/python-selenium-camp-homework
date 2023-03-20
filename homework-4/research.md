## HTML Nedir?

HTML(Hyper Text Markup Language) bir web sayfasının yapısını belirleyen bir dildir. HTML ile yazılan kodlar web
tarayıcılarının anlayacağı şekilde derlenir ve web sayfası oluşturulur.

HTML kodları, bir web sitesinin yapısını belirleyen etiketlerden oluşur. Etiketler, bir web sayfasının içeriğinin ne
olduğunu, görünümünün nasıl olacağını ve web sayfasının nasıl çalışacağını belirler.

HTML etiketleri, `<` ve `>` karakterleri arasına alınır. Örneğin, bir başlık etiketi şu şekilde görünür:

```html
<h1>Bu bir başlık</h1>
```

## HTML Locators

Selenium IDE, HTML kodlarını bulmak için HTML locators kullanır. HTML locators, bir web sayfasındaki bir öğenineri
bulmak için kullanılan bir yöntemdir. Bu yöntemde, bir öğenin HTML kodlarına bakılır ve öğenin özellikleri
kullanılarak bir XPath veya CSS seçicisi oluşturulur.

Selenium IDE, HTML locators'ı otomatik olarak oluşturur. Bu, Selenium IDE'nin, HTML kodlarını otomatik olarak
tarayarak öğeleri bulmasını sağlar.

## HTML Locator Tipleri

Selenium IDE, 8 farklı HTML locator tipi kullanır:

* ID
* Name
* Class Name
* Tag Name
* Link Text
* Partial Link Text
* CSS Selector
* XPath

### ID

ID, öğenin benzersiz bir kimliği sağlar.

Örneğin, bir button öğesinin HTML kodları şu şekilde görünebilir:

```html

<button id="button1">Tıkla</button>
```

Bu öğenin ID'si `button1`'dir.

### Name

Name, bir öğenin adını belirtir.

Örneğin, bir button öğesinin HTML kodları şu şekilde görünebilir:

```html

<button name="button1">Tıkla</button>
```

Bu öğenin adı `button1`'dir.

### Class Name

Class Name,bir öğenin sınıf adını belirtir.

Örneğin, bir button öğesinin HTML kodları şu şekilde görünebilir:

```html

<button class="button1">Tıkla</button>
```

Bu öğenin sınıf adı `button1`'dir.

### Tag Name

Tag Name,bir öğenin etiket adını belirtir.

Örneğin, bir button öğesinin HTML kodları şu şekilde görünebilir:

```html

<button>Tıkla</button>
```

Bu öğenin etiket adı `button`'dır.

### Link Text

Link Text, bir öğenin metin içeriğini belirtir.

Örneğin, bir link öğesinin HTML kodları şu şekilde görünebilir:

```html
<a href="https://www.google.com">Google</a>
```

Bu öğenin metin içeriği `Google`'dır.

### Partial Link Text

Partial Link Text, bir öğenin metin içeriğinin bir kısmını belirtir.

Örneğin, bir link öğesinin HTML kodları şu şekilde görünebilir:

```html
<a href="https://www.google.com">Google</a>
```

Bu öğenin metin içeriğinin bir kısmı `Goo`'dır.

### CSS Selector

CSS Selector, bir öğenin HTML kodlarındaki yoluyla bir öğeyi bulmaya yarayan bir seçicidir.

Örneğin, bir button öğesinin HTML kodları şu şekilde görünebilir:

```html

<html>
<body>
<button id="button1">Tıkla</button>
</body>
</html>
```

Bu öğenin CSS seçicisi `html > body > button`'dır.

### XPath

XPath, bir öğenin HTML kodlarındaki yoluyla bir öğeyi bulmaya yarayan bir seçicidir.

Örneğin, bir button öğesinin HTML kodları şu şekilde görünebilir:

```html

<html>
<body>
<button id="button1">Tıkla</button>
</body>
</html>
```

Bu öğenin XPath'i `/html/body/button`'dır.

## Selenium Aksiyonları

Selenium IDE aşağıdaki aksiyonları destekler:

* **build()** : Selenium IDE'nin HTML locators'ı oluşturmasını sağlar.
* **click()** : Bir öğeye tıklar.
* **clickAndHold()** : Bir öğeye tıklar ve basılı tutar.
* **contextClick()** : Bir öğeye sağ tıklayarak tıklar.
* **doubleClick()** : Bir öğeye çift tıklar.
* **dragAndDrop()** : Bir öğeyi sürükler ve bırakır.
* **keyDown()** : Bir tuşa basılı tutar.
* **keyUp()** : Bir tuşu bırakır.
* **moveByOffset()** : Fareyi bir öğenin üzerindeki bir noktaya taşır.
* **moveToElement()** : Fareyi bir öğenin üzerine taşır.
* **pause()** : Testi duraklatır.
* **perform()** : Bir aksiyonu gerçekleştirir.
* **release()** : Bir öğeyi bırakır.
* **scrollByAndOffset()** : Bir öğenin üzerindeki bir noktaya kaydırır.
* **scrollToElement()** : Bir öğenin üzerine kaydırır.
* **sendKeys()** : Bir öğeye bir tuşa basarak bir metin gönderir.
* **tick()** : Bir işaret kutusunu işaretler.
