<!--
*** Thanks for checking out this project. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
***
-->


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/reoyamanaka/requestsAuthentication.git">
    <img src="images/padlock.gif" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">POST & GET demonstrations using Requests</h3>

  <p align="center">
    A Python program that uses the Requests module and httpbin.org to test POST and GET submissions in practical use-cases.
    <br />
    <a href="https://github.com/reoyamanaka/requestsAuthentication"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#usage">View Demo</a>
    ·
    <a href="https://github.com/reoyamanaka/requestsAuthentication/issues">Report Bug</a>
    ·
    <a href="https://github.com/reoyamanaka/requestsAuthentication/issues">Request Feature</a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

There are several ways you can employ Python's <b>request module</b> using this program.
<ul>
  <li>Standard GET request with two arbitrary parameters <i>page number</i> and <i>count</i></li>
  <li>Standard POST request with two arbitrary parameters <i>username</i> and <i>password</i></li>
  <li>Simulate server authentication using a POST request</li>
  <li>Test connection timeout by simulating the loading time</li>
</ul>

### Built With

* macOS Big Sur Version 11.2.3
* Adobe Illustrator Version 23.1 (Logo design)
* Python 3.9.1

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* requests
  ```sh
  pip3 install requests
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/reoyamanaka/requestsAuthentication.git
   ```
2. Install requirements
   ```sh
   pip3 install -r requirements.txt
   ```

<!-- USAGE -->
## Usage

### Testing GET request

![](images/get.gif)

### Testing POST request

![](images/post.gif)

### Testing POST request for authentication (with valid credentials)

![](images/validAuth.gif)

### Testing POST request for authentication (with invalid credentials)

![](images/invalidAuth.gif)

### Testing connection timeout

![](images/timeout.gif)


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/reoyamanaka/requestsAuthentication/issues) for a list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the GNU Affero General Public License v3.0 License. See `LICENSE` for more information.


<!-- CONTACT -->
## Contact

Reo Yamanaka - [LinkedIn](https://www.linkedin.com/in/reo-yamanaka-7a2289119/) - [My YouTube channel](https://www.youtube.com/channel/UCBwqp_MEM2XcSnq7kRvOB3A) - ryamanaka807@gmail.com

Project Link: [https://github.com/reoyamanaka/requestsAuthentication.git](https://github.com/reoyamanaka/requestsAuthentication.git)
