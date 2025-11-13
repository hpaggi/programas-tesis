# Fusion Holónica de Información

Repositorio asociado a la tesis doctoral de Horacio Paggi y a las publicaciones científicas derivadas de la misma. La [tesis doctoral](https://oa.upm.es/54198/) lleva por título "Modelo de fusión holónica de información para la mejora de la calidad de la información en redes peer-to-peer con recursos limitados", y está dirigida por los profesores Javier Soriano y Juan A. Lara. En la tesis doctoral se presenta un modelo que fusiona información, aplicando principios holónicos, con el objetivo de mejorar la calidad de la información en redes que disponen de recursos limitados.

En cuanto a las publicaciones científicas derivadas de la tesis, entre otras, se encuentra el artículo que lleva por título "Structures generated in a multiagent system performing information fusion in peer-to-peer resource-constrained networks" publicado en el journal [Neural Computing and Applications](https://doi.org/10.1007/s00521-018-3818-1). En esta publicación, se describen los mecanismos propuestos para la generación de holones en el modelo de fusión de información planteado, presentando las ventajas de dichas estructuras holónicas.

## Código

En el respositorio se encuentran los programas python usados generar datos en la investigación realizada. Muchas veces un programa se repite con pequeñas variaciones, ya que se hicieron numerosos experimentos con distintas configuraciones de los parámetros. Los programas con nombre "simulador*" son los que simulaban la ejecución del MAS con distintos valores de los parámetros. Los denominados "analizador*" son los que analizaban los logs generados por el simulador usado.

## Datos

A lo largo de la tesis doctoral y sus publicaciones asociadas, se presentaron casos de estudio a partir del dataset "Car Evaluation" con DOI [10.24432/C5JP48](http://archive.ics.uci.edu/dataset/19/car+evaluation) con información relativa a vehículos, proporcionado en el Machine Learning Repository de la UC Irvine. 

## Estructura del repositorio

```
├── *.py        # Python scripts used
├── LICENSE     # Code license
└── README.md   # Project summary
```

## Referencias

Paggi, H., Lara, J.A. & Soriano, J. Structures generated in a multiagent system performing information fusion in peer-to-peer resource-constrained networks. Neural Comput & Applic 32, 16367–16385 (2020). https://doi.org/10.1007/s00521-018-3818-1. DOI: [10.1007/s00521-018-3818-1](https://doi.org/10.1007/s00521-018-3818-1).

```tex
@article{Paggi_2018,
   title={Structures generated in a multiagent system performing information fusion in peer-to-peer resource-constrained networks},
   volume={32},
   ISSN={1433-3058},
   url={http://dx.doi.org/10.1007/s00521-018-3818-1},
   DOI={10.1007/s00521-018-3818-1},
   number={21},
   journal={Neural Computing and Applications},
   publisher={Springer Science and Business Media LLC},
   author={Paggi, Horacio and Lara, Juan A. and Soriano, Javier},
   year={2018},
   month=oct, pages={16367–16385}}

```
