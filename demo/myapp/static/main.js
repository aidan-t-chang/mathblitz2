var player_username = "Johnson";

var totalwins = 150;
var totallosses = 25;
var fastestroundt = 35;

var rankedwins = 121;
var rankedlosses = 5;
var fastestroundr = 40;

var caswins = 29;
var caslosses = 20;
var fastestroundc = 35;

document.getElementById("options").addEventListener("change", function() {
    let selectedValue = this.value;
    let contentDiv = document.getElementById("content");

    switch(selectedValue) {
        case "option1":
            getStats(1);
            break;
        case "option2":
            getStats(2); 
            break;
        case "option3":
            getStats(3);
            break;
        default:
            contentDiv.textContent = "Selected option will appear here.";
    }
});

function getStats(option) {
    document.getElementById('content').innerHTML = '';
    if (option == 1) { // total
        togames = document.createElement('p');
        ff = totalwins + totallosses;
        togames.textContent = "Total Games Played: " + ff + " games";
        towins = document.createElement('p');
        towins.textContent = "Total Wins: " + totalwins + " wins";
        tolosses = document.createElement('p');
        tolosses.textContent = "Total Losses: " + totallosses + " losses";
        towlratio = document.createElement('p');
        let ratio = totalwins / totallosses;
        towlratio.textContent = "W/L Ratio: " + ratio;
        fotal = document.createElement('p');
        fotal.textContent = "Fastest Round (Total): " + fastestroundt + "s";
        document.getElementById('content').appendChild(togames);        
        document.getElementById('content').appendChild(towins);        
        document.getElementById('content').appendChild(tolosses);        
        document.getElementById('content').appendChild(towlratio);        
        document.getElementById('content').appendChild(fotal);        
    }
    else if (option == 2) {
        ragames = document.createElement('p');
        add = rankedwins + rankedlosses;
        ragames.textContent = "Ranked Games Played: " + add + " games";
        rawins = document.createElement('p');
        rawins.textContent = "Ranked Wins: " + rankedwins + " wins";
        ralosses = document.createElement('p');
        ralosses.textContent = "Ranked Losses: " + rankedlosses + " losses";
        rawlratio = document.createElement('p');
        let ratio = rankedwins / rankedlosses ;
        rawlratio.textContent = "Ranked W/L Ratio: " + ratio;
        ratotal = document.createElement('p');
        ratotal.textContent = "Fastest Round (Ranked): " + fastestroundr + "s";
        document.getElementById('content').appendChild(ragames);        
        document.getElementById('content').appendChild(rawins);        
        document.getElementById('content').appendChild(ralosses);        
        document.getElementById('content').appendChild(rawlratio);        
        document.getElementById('content').appendChild(ratotal);
    }
    else {
        cagames = document.createElement('p');
        cc = caswins + caslosses;
        cagames.textContent = "Casual Games Played: " + cc + " games";
        cawins = document.createElement('p');
        cawins.textContent = "Casual Wins: " + caswins + " wins";
        calosses = document.createElement('p');
        calosses.textContent = "Casual Losses: " + caslosses + " losses";
        cawlratio = document.createElement('p');
        let ratio = caswins / caslosses;
        cawlratio.textContent = "Casual W/L Ratio: " + ratio;
        catotal = document.createElement('p');
        catotal.textContent = "Fastest Round (Casual): " + fastestroundc + "s";
        document.getElementById('content').appendChild(cagames);        
        document.getElementById('content').appendChild(cawins);        
        document.getElementById('content').appendChild(calosses);        
        document.getElementById('content').appendChild(cawlratio);        
        document.getElementById('content').appendChild(catotal);
    }
}

function getUsername() {
    dave = document.createElement('h2');
    dave.textContent = player_username;
    document.getElementById('columnmid').innerHTML = "";
    document.getElementById('columnmid').appendChild('dave');
}

getUsername();