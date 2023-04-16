///////////////////////
// Author: Minghao Zhao
// Date: 4-15-2023
///////////////////////

// This file will save the returned json to mongodb

const mongoose = require("mongoose");
const Schema = mongoose.Schema; 
const fs = require('fs');

// Change the end point to your own
mongoose.connect("mongodb://localhost:27017/enzydb");

let mdd = new Schema({
    runtime: {
        type: []
    },
    configuration : {
        type: []
    }
})

let ligandd = new Schema({
    smiles: {
        type: String
    },
    cif: {type: String}
    ,
    binding: {type: String},
    binding_method: {
        type: []
    }
})

let inside = new Schema({
    mdConfig: {
        type: mdd
    }, 
    traj: {
        type: []
    },
    Structure: {
        type: []
    },
    ligand: {
        type: ligandd
    },
    sequence: {
        type: String
    }

})


let enzy = new Schema({
    name: {type: String},
    content: {type: inside}
})

const db = mongoose.model("enzy", enzy);
const data = fs.readFileSync('result.json', 'utf8');
jsond = JSON.parse(data)
for (let d in jsond) {
    console.log(jsond[d].structure)
    console.log("saving")
    const newE = new db({
        name: d, 
        content: {sequence: jsond[d].sequence,
            Structure: jsond[d].structure,
                  traj: jsond[d].traj,
                  mdConfig: {
                    runtime: jsond[d]["md-conig"]["runtime-config"],
                    configuration: jsond[d]["md-conig"]["md-configuration"]
                  },
                  ligand: {
                    smiles: jsond[d]["ligand"]["smiles"],
                    cif: jsond[d]["ligand"]["cif"],
                    binding: jsond[d]["ligand"]["binding"],
                    binding_method: jsond[d]["ligand"]["binding_method"]
                  }
                }


    })
    newE.save();
}