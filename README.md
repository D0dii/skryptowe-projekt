# Blog Application

## Opis projektu

Aplikacja blogowa umożliwia użytkownikom tworzenie kont, logowanie, pisanie postów, komentowanie, polubienia postów oraz śledzenie innych użytkowników. Poniżej znajduje się opis struktury projektu oraz najważniejszych funkcji.

## Struktura projektu

### URLs

Plik `urls.py` definiuje ścieżki URL, które mapują różne widoki w aplikacji. Każda ścieżka jest przypisana do konkretnej funkcji widoku, która jest wywoływana, gdy użytkownik odwiedza daną stronę.

### Widoki (Views)

W pliku `views.py` definiujemy logikę aplikacji. Tutaj znajdują się funkcje, które odpowiadają na żądania HTTP. Przykłady widoków to wyświetlanie listy postów, tworzenie nowego posta, edycja posta, wyświetlanie szczegółów posta oraz obsługa polubień.

### Modele (Models)

Plik `models.py` zawiera definicje modeli danych. Modele to struktury danych, które odpowiadają tabelom w bazie danych. Przykłady modeli to `Post`, `Comment`, `Profile`, które reprezentują posty, komentarze i profile użytkowników.

### Formularze (Forms)

Plik `forms.py` zawiera definicje formularzy. Formularze są używane do zbierania danych od użytkowników, takich jak dane rejestracyjne, logowania, tworzenia i edycji postów.

### Szablony (Templates)

Folder `templates` zawiera pliki HTML, które definiują wygląd aplikacji. Szablony są renderowane przez widoki i wyświetlane użytkownikom. Przykłady szablonów to `index.html`, `post_detail.html`, `base_generic.html`.

### Statyczne pliki (Static Files)

Folder `static` zawiera statyczne pliki, takie jak CSS, JavaScript i obrazy, które są używane do stylizacji i interaktywności aplikacji.

### Media

Folder `media` zawiera przesyłane przez użytkowników pliki, takie jak zdjęcia profilowe.

### Plik `settings.py`

Plik `settings.py` zawiera konfigurację projektu Django, taką jak konfiguracja bazy danych, ustawienia statycznych i medialnych plików oraz inne ustawienia specyficzne dla projektu.

### Plik `urls.py`

Główny plik `urls.py` w folderze projektu zawiera globalne ścieżki URL, które mogą również zawierać odniesienia do plików `urls.py` poszczególnych aplikacji w projekcie.

## Funkcjonalności

### Tworzenie i edycja konta użytkownika

Użytkownicy mogą rejestrować się i logować do aplikacji. Formularze rejestracji i logowania są definiowane w `forms.py`, a logika obsługi tych formularzy znajduje się w `views.py`.

### Tworzenie, edycja i usuwanie postów

Użytkownicy mogą tworzyć nowe posty, edytować istniejące posty oraz je usuwać. Formularze do tworzenia i edycji postów są definiowane w `forms.py`, a logika obsługi tych operacji znajduje się w `views.py`.

### Polubienia postów

Użytkownicy mogą polubić posty innych użytkowników. Relacja `ManyToMany` między użytkownikami a postami jest zdefiniowana w `models.py`, a logika obsługi polubień znajduje się w `views.py`.

### Komentowanie postów

Użytkownicy mogą komentować posty. Komentarze są zdefiniowane jako osobny model w `models.py`, a formularze do tworzenia komentarzy znajdują się w `forms.py`.

### Śledzenie użytkowników

Użytkownicy mogą śledzić innych użytkowników. Relacja `ManyToMany` między użytkownikami jest zdefiniowana w modelu `Profile` w `models.py`, a logika obsługi tej funkcji znajduje się w `views.py`.

### Wyszukiwanie

Użytkownicy mogą wyszukiwać posty na podstawie tytułu, autora i tagów. Formularz wyszukiwania jest zdefiniowany w `forms.py`, a logika obsługi wyszukiwania znajduje się w `views.py`.

## Podsumowanie

Projekt ten demonstruje, jak można zbudować w pełni funkcjonalną aplikację blogową za pomocą frameworka Django. Każdy aspekt aplikacji, od modeli danych po szablony i logikę widoków, jest starannie zdefiniowany, aby zapewnić spójne i wydajne działanie.
