| extension         | package     | method                                         |
|-------------------|-------------|------------------------------------------------|
| .tar   	          | tarfile	    | tarfile.open(file, 'r').extractall(path)       |
| .tar.gz /  .tgz	  | tarfile     | 	tarfile.open(file, 'r:gz').extractall(path)   |
| .tar.bz2 / .tbz2	 | tarfile     | 	tarfile.open(file, 'r:bz2').extractall(path)  |
| .tar.xz /  .txz	  | tarfile     | 	tarfile.open(file, 'r:xz').extractall(path)   |
| .zip	             | zipfile	    | zipfile.ZipFile(file, 'r').extractall(path)    |
| .gz	              | gzip	       | gzip.open(file, 'rb').read()                   |
| .bz2   	          | bz2	        | bz2.open(file, 'rb').read()                    |
| .xz	              | lzma	       | lzma.open(file, 'rb').read()                   |
| .rar   	          | rarfile	    | rarfile.RarFile(file).extractall(path)         |
| .7z	              | py7zr	      | py7zr.SevenZipFile(file, 'r').extractall(path) |
| .Z	               | unlzw	      | unlzw(file, output_file)                       |
| .arj	             | patool	     | patoolib.extract_archive(file, outdir=path)    |
| .cab	             | cabextract	 | cabextract.CabFile(file).extractall(path)      |

extra requirements: `rarfile py7zr patool unlzw`
