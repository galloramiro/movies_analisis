# movies_analisis
This project is not focused on an in-depth analysis of the dataset, but rather on how to create tools that will help us automate the work with the archive, and to be able to scale it in a simple way.

In order to avoid problems with the environment, the project was put in a docker, in which the necessary libraries could be installed for any analysis project that we want to do. 

To store the data we work with, we created a data folder. This way the scripts can point to it and keep the work organized. At the same time this folder is excluded in gitignore to avoid uploading large files.

To store our analysis services we created a folder called service, which will contain the constants, the factories and a folder for each service.

In this case, the film analysis service separates it into three files:
- [files_handlers.py](https://github.com/galloramiro/movies_analisis/blob/master/work/analizers/services/movies/files_handlers.py#L1)  
  It contains the classes in charge of handling the files, this implies processing and necessary transformations to be able to be used later with the plotting tools. 
- [plotter.py](https://github.com/galloramiro/movies_analisis/blob/master/work/analizers/services/movies/ploter.py#L1)  
  Contains the classes in charge of creating the different graphs, in this case there are two, one that uses Seaborn to create static data, and another that uses Altair to create dynamic graphs, both use the same names in the functions which allows the service to be independent of them and can use any of them. 
- [service.py](https://github.com/galloramiro/movies_analisis/blob/master/work/analizers/services/movies/service.py#L1)  
  Here is the class in charge of the logic that allows us to get the charts we need for the analyses. The more possibilities exist in the other two, the more this can be extended. 

Finally, in the root of the services folder we will find the [factories.py](https://github.com/galloramiro/movies_analisis/blob/master/work/analizers/services/factories.py#L1) file which allows us to access a factory that can create our services, in this case a static analysis service and another dynamic analysis service.  


### Environment instalation
```bash
$ cd docker
$ bash build_docker.sh
$ bash run_docker.sh
```

### [Play with the current service](https://github.com/galloramiro/movies_analisis/blob/master/work/analizers/0-movies-analisis.ipynb)
