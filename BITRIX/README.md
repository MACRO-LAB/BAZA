<div style="text-align: center">
    <h1>BITRIX</h1>
</div>

## Event
<details>
<summary>Обработчик события `OnAfterIBlockElementUpdate`
</summary>

[OnAfterIBlockElementUpdate](event/OnAfterIBlockElementUpdate.php)

### Основные функции
1. **Проверка инфоблока**: Скрипт работает только с элементами инфоблока с ID = 8 (например, инфоблок "Новости").
2. **Извлечение изображений**: Скрипт ищет в поле `DETAIL_TEXT` теги `<img>` с изображениями, закодированными в
   формате Base64.
3. **Сохранение изображений**: Изображения декодируются из Base64 и сохраняются на сервере в директории
   `upload/news/{ID элемента}/`.
4. **Обновление текста**: После сохранения изображений, ссылки на них в поле `DETAIL_TEXT` заменяются на пути к
   сохраненным файлам.
5. **Очистка старых изображений**: Скрипт удаляет изображения из директории, которые больше не упоминаются в поле
   `DETAIL_TEXT`.

</details>


## Other
<details>
  <summary>logger</summary>

[logger](logger/logger.php)
</details>


<details>
  <summary>smtp_mail</summary>

[smpt_mail](smtp_mail)
</details>


<details>
  <summary>пример вывода элементов инфоблока с названием раздела \Bitrix\Main\Loader::includeModule('iblock');</summary>

```php
\Bitrix\Main\Loader::includeModule('iblock');
     function apiGetData($url)
         //подключение и декодирование API ссылки
     {
         $data = file_get_contents($url);
         $characters = json_decode($data, true);
         return $characters;
     }

     $iblockId = 'tasks';
     $arSelect = array(
         'ID',
         'ACTIVE',
         'NAME',
         'IBLOCK_CODE',
         'PROPERTY_SLIDE_SHOW_CONDITION',
         'PROPERTY_SLIDE_SHOW_DAY',
         'PROPERTY_API_SLIDE',
         'PROPERTY_TYPE_COUNT',
         'IBLOCK_SECTION_ID',
     );
     $arFilter = array("IBLOCK_CODE" => $iblockId);
     $res = \CIBlockElement::GetList(array(), $arFilter, false, false, $arSelect);

     $arResult = array();

     $cacheTime = 60*60*12; // время кеширования в секундах
     $cacheId = 'cache_api_tasks'; // уникальный идентификатор кеша

     $obCache = \Bitrix\Main\Data\Cache::createInstance();
     if($obCache->InitCache($cacheTime, $cacheId))
     {
         return $arResult = $obCache->GetVars();
     }elseif($obCache->StartDataCache())
     {
         while ($arFields = $res->GetNext())
         {
             $sectionId = $arFields['IBLOCK_SECTION_ID'];
             $sectionRes = \CIBlockSection::GetList(array(), array('ID' => $sectionId));
             $sectionFields = $sectionRes->GetNext();
             $arFields['SECTION_NAME'] = $sectionFields['NAME'];
             if (!empty($arFields['PROPERTY_API_SLIDE_VALUE']))
             {
                 $arFields['API_DATA'] = apiGetData($arFields['PROPERTY_API_SLIDE_VALUE']);
             }
             $arResult[] = $arFields;
         }
         $obCache->EndDataCache($arResult);

     }
     return $arResult;
```
</details>


<details>
  <summary>Если мы хотим использовать классы Битрикса, но не хотим выводить визуальную часть </summary>
    вместо подключения  вначале и  вконце

```php
   require($_SERVER["DOCUMENT_ROOT"]."/bitrix/header.php");
   require($_SERVER["DOCUMENT_ROOT"]."/bitrix/footer.php");
```
можно просто подключить
```php
   \Bitrix\Main\Loader; Loader::includeModule('iblock');
   require($_SERVER["DOCUMENT_ROOT"]."/bitrix/modules/main/include/prolog_after.php");
   require($_SERVER["DOCUMENT_ROOT"]."/bitrix/modules/main/include/prolog_before.php"); 
```
</details>


<details>
  <summary>пример добавления имени раздела в catalog.item  с cache</summary>

```php
   ["IBLOCK_ID" => $sectionId];
       $arSelect = ['ID', 'NAME'];
       $sectionRes = \Bitrix\Iblock\SectionTable::getList([
           'filter' => $arFilter,
           'select' => $arSelect,
           'cache' => ['ttl' => 86400],
       ])->fetch();
       $arResult['ITEM']['SECTION_SAME'] = $sectionRes['NAME'];
```
</details>


<details>
  <summary>пример с SectionTable</summary>

```php
	 $sectionRes = \Bitrix\Iblock\SectionTable::getList([
		'select' => ['ID', 'NAME'],
	])->fetchAll();
	foreach ($arResult['ITEMS'] as &$arItem)
	{
		foreach ($sectionRes as $section)
		{
			if ($section['ID'] == $arItem['IBLOCK_SECTION_ID'])
			{
				$arItem['SECTION_NAME'] = $section['NAME'];
			}
		}
		unset($arItem);
	}
```
</details>


<details>
  <summary>получить данные о шаблоне</summary>

```php
 	bitrix/modules/main/classes/general/component_template.php
  	pr($this->__file);  745 row

```
</details>


<details>
  <summary>PHP строка в админке пример проверки 1с url	</summary>

```php
   <?php
   $http = new Main\Web\HttpClient();
   $http->disableSslVerification();
   $http->setRedirect(false);
   $http->setHeader('Content-Type', 'application/json; charset=UTF-8');
   //		$http->setHeader('Authorization', 'Bearer nmDh27tpEWzhyi4');
   
   var_dump($http->post('http://89.108.118.100:31900/mixcar_ut_router/hs/reciever/mixcar_ut/',
       Main\Web\Json::encode($data, JSON_UNESCAPED_UNICODE)));
   
   var_dump($http->getError());
   ?>
```
</details>
