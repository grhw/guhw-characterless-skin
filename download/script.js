const apiUrl = `https://api.github.com/repos/grhw/guhw-characterless-skin/releases`;

async function fetchReleases() {
    try {
        const response = await fetch(apiUrl);
        const releases = await response.json();
        displayReleases(releases);
    } catch (error) {
        console.error("Error:", error);
        document.querySelectorAll(".releases").innerHTML = `<p>Error loading releases.</p>`;
    }
}

function displayReleases(releases) {
    const releasesList = document.querySelector(".releases");

    releases.forEach((release,index) => {
        if (release.assets.length < 1) return;
        const element = document.querySelector(".release").cloneNode(true)
        const version = element.querySelector(".version")

        version.innerText = release.tag_name
        element.addEventListener("click",()=>{
            downloadFile(release.assets[0].browser_download_url, release.tag_name)
        })

        releasesList.appendChild(element)
    });
}

function downloadFile(url, tag) {
    const link = document.createElement("a");
    link.href = url;
    link.download = `[${tag}] guhw's insta-fading read.osk`; // The browser might not honor this due to CORS
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}



fetchReleases();