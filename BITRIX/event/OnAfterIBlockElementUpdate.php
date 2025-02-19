<?php
addEventHandler('iblock', 'OnAfterIBlockElementUpdate', 'myFunction');
function myFunction(&$arFields)
{
	//только для инфоблока news
	if ($arFields['IBLOCK_ID'] == 8)
	{
		$el = new CIBlockElement();
		if (strrpos($arFields['DETAIL_TEXT'], 'data:image/'))
		{
			//для проверки форматов
			$format = ['jpeg', 'jpg', 'gif', 'png', 'bmp'];

			$tmp = SITE_DIR.'upload/news/';


			$matchesW = [];
			// Получаем значение атрибута src из тега <img>
			preg_match_all('/<img[^>]+>/', $arFields['DETAIL_TEXT'], $matchesW);
			$allBaseImg = [];
			foreach ($matchesW[0] as $imgTag)
			{
				$src = preg_match('/src="([^"]+)"/', $imgTag, $matches2) ? $matches2[1] : '';
				$allBaseImg[] = [
					'DATA_IMG' => $src,
					'NAME_IMG' => '',
					'TYPE_IMG' => '',
				];
			}

			foreach ($allBaseImg as &$imgTag)
			{
				if (strpos($imgTag['DATA_IMG'], 'data:image/') !== 0)
				{
					continue;
				}

				//формат картинки
				$imageType = substr($imgTag['DATA_IMG'], strpos($imgTag['DATA_IMG'], '/') + 1,
					strpos($imgTag['DATA_IMG'], ';') - strpos($imgTag['DATA_IMG'], '/') - 1);
				$imgTag['TYPE_IMG'] = $imageType;

				if (in_array($imgTag['TYPE_IMG'], $format) === false)
				{
					continue;
				}

				//имя картинки
				$filename = uniqid('detaiTextImage') . '.' . $imageType;
				$imgTag['NAME_IMG'] = $filename;

				//раскодированная картинка
				$imageData = base64_decode(preg_replace('#^data:image/\w+;base64,#i', '', $imgTag['DATA_IMG']));

				//сохраняем картинку
				$obFile =
					new \Bitrix\Main\IO\File(\Bitrix\Main\Application::getDocumentRoot() . $tmp . $arFields['ID'] . '/'
						. $filename);
				$obFile->putContents($imageData);

				//заменяем путь к картинке в тексте
				$arFields['DETAIL_TEXT'] = str_replace($imgTag['DATA_IMG'], $tmp . $arFields['ID'] . '/' . $filename,
					$arFields['DETAIL_TEXT']);
			}

			// Удаляем файлы, которых нет в поле DETAIL_TEXT
			$obFileDel =
				new \Bitrix\Main\IO\File(\Bitrix\Main\Application::getDocumentRoot() . $tmp . $arFields['ID'] . '/');
			$fileDir = scandir($obFileDel->getPath());

			foreach ($fileDir as $file)
			{
				if ($file !== '.' && $file !== '..')
				{
					if ((strripos($arFields['DETAIL_TEXT'], $file)) == false)
					{
						unlink($obFileDel->getPath() . '/' . $file);
					}
				}
			}
			$el->Update($arFields['ID'], $arFields);
		}

	}
}

