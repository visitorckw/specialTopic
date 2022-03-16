<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h1 align="center">Special Topic</h1>

  <p align="center">
    <br />


</p>
</div>
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is our special topic project for NCKU SCIE.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With


* [Node.js](https://nodejs.org/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Nginx](https://www.nginx.com/)
* [Mysql](https://www.mysql.com/)
* [Docker](https://www.docker.com/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started


Our project is based on docker and docker-compose

### Prerequisites

Before running docker-compose, you'll need to have docker and docker-compose installed on linux computer already
* docker
  ```sh
  sudo apt-get install docker.io
  ```
* docker-compose
  ```sh
  sudo curl -L "https://github.com/docker/compose/releases/download/v2.2.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  sudo chmod +x /usr/local/bin/docker-compose
  ```

### Installation

Below is an example of installing and setting up the project.

1. Clone the repo
   ```sh
   git clone https://github.com/visitorckw/specialTopic.git
   ```
3. Change directory to the project
   ```sh
   cd specialTopic
   ```
4. Build and run the project
   ```sh
   sudo docker-compose up -d --build
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
Below is an example of running the project.
* Start server
   ```sh
   sudo docker-compose up -d
   ```
* Stop server
   ```sh
   sudo docker-compose down
   ```


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

There is currently no license for the project

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

visitorCKW - visitorckw@gmail.com

Project Link: [https://github.com/visitorckw/specialTopic](https://github.com/visitorckw/specialTopic)

<p align="right">(<a href="#top">back to top</a>)</p>
