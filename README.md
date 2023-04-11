# TugasPyBootcamp
Cara mengupload tugas ke github https://github.com/fahrilshaputraa/TugasPyBootcamp

1. [Buat Fork Baru](#buat-fork-baru)
2. [Git Clone](#git-clone)
3. [Buka VSCode](#buka-vscode)
4. [Pull Request Manual](#pull-request-manual)

### Keterangan
Gambar hanya sekedar referensi⚠️

## Buat Fork Baru
Sesudah kalian masuk link yang diatas kalian dapat mengklik fork yang terdapat di ujung kanan dekat profile.


<img src="image/2023-04-10 (1).png">

Klik pada button tersebuh, kemudian kalian un ceklis Copy the ```master``` branch only

<img src="image/2023-04-10 (2).png">

Lanjut klik "**Create fork**"

## Git Clone
Pada menu ```<>code``` terdapat button "**<>Code**" klik button tersebut, lanjut akan terdapat link dan salin link tersebut

<img src="image/2023-04-10 (4).png">

Sesudah kalian salin, lanjut buka file exploler di laptop/pc kalian masing-masing, kemudian kalian pilih dimana kalian akan mengclone folder tersebut lalu klik kanan pada mouse pilih "**Open in Terminal**" tunggu sesaat sampai terminal kalian terbuka.

<img src="image/2023-04-10 (5).png">

Jika sudah masuk lanjut ketik 
```bash
$ https://github.com/fahrilshaputraa/TugasPyBootcamp.git
# untuk masuk foldernya
$ cd TugasPyBootcamp/
# untuk membuka di VSCode
$ code .
```
<img src="image/2023-04-10 (9).png">


## Buka VSCode
Buka folder di Visual Studio Code dengan terminal menggunakan ```code .``` di folder yang ingin kalian buka contoh seperti yang di atas↑
Sesudah masuk tambahkan folder sesuai nama anda, dan di dalamnya terdapat tugas yang sudah anda kerjakan.

<img src="image/2023-04-10 (12).png">

Kemudian kalian buka terminal dengan menggunakan ```ctrl + shift + ` ``` atau bisa secara manual seperti dibawah ini.

<img src="image/2023-04-10 (14).png">

Lalu di terminal tersebut kalian masukan perintah

``` bash
$ git checkout -b Tugas
```
Lanjut tambahkan perintah berikut

``` bash
$ git add .
```
Kemudian

``` bash
$ git commit -m "<isi pesan>
```
dan yang terakhir
``` bash
$ git push origin Tugas
# "Tugas" tersebut harus sama sesuai apa yang pertama di buat contoh punya saya membuat awalnya adalah Tugas maka ketika akan git push harus sesuai.
```
Bisa dilihat digambar di bawah iniↆ

<img src="image/2023-04-10 (17).png">
<img src="image/2023-04-10 (18).png">

Ketika sudah seperti ini maka ```git push``` sudah berhasil.
Lalu kalian buka github masing masing jika ada pesan "**Create pull request**" klik pesan tersebut.

## Pull Request Manual
Namun jika tidak ada pesan "**Create pull request**" kita bisa membuatnya secara manual, dengan cara:
klik seperti gambar yang sudah terdapat garis

<img src="image/2023-04-10 (20).png">

Sesudah masuk akan terdapat button "**Create pull request**"

<img src="image/2023-04-10 (21).png">

Lanjut akan terdapat keterangan seperti berikut

<img src="image/2023-04-10 (22).png">

Klik saja button "**Create pull request**", atau jika kalian ingin mengubah title dari apa yang tadi di ```git push``` itu silahkan sesuaikan saja.

Sesudah itu klik "**Merge pull request**"

<img src="image/2023-04-10 (23).png">

Sampai terdapat button "**Confirm merge**"

<img src="image/2023-04-10 (24).png">

*"**Confirm merge**" klik saja, dan tunggu beberapa saat samapi yang awal mulanya berwarna hijau jadi warna ungu. Tunggu samapi di Confirmasi oleh yang mempunyai akses dan jika sudah maka folder anda akan masuk kedalam repository tersebut.*
