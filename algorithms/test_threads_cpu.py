import mutate
import numpy as np

dna = 'actgatcgatcgatcgtcagctactgcatcgatcacgtgacgtatcatcgcatgctacgtagctacgtacgtacgactcgatgcatcgactgatgctacgtagctagctgatcgatcagtacgtacgtagctagctgcagcatcgatgcatagtcgatcgcatgcatgcatagtcgactacgtacgtagctgactgactgactgactacgatcgactgactacgggtgactaaaaaaaaacacacaccccacacacacacacacatactactatcactacgactcgatgagagaagtgaactacgagtcacagatgcatacagatgatgatagatagctagcatgatagcatgcagaagaactgatatctacacgtacgtactgactgacgtactgactgactgactgactgacgtacgtacgtactgacgtactgacgtacgtacgtactgactgacgtacgtacgtacgtacgtactactgacgtacgtacactgacgtacgtacgtactactacacgtactgactacgtacgtacgtacgtactcatctgactgactgactcgtactactacgtactactacgtactgactgactactgactgactgatcatagtatggcgcgcgcgcgacgtacgtcagtcagctgtcagctgtacgatgctgctagcagtcagactgactacgtacgtcagatgatgatgctagccatgctagtacgatgactgactacgatcgactgatcgatcgatcgtcagctactgcatcgatcacgtgacgtatcatcgcatgctacgtagctacgtacgtacgactcgatgcatcgactgatgctacgtagctagctgatcgatcagtacgtacgtagctagctgcagcatcgatgcatagtcgatcgcatgcatgcatagtcgactacgtacgtagctgactgactgactgactacgatcgactgactacgggtgactaaaaaaaaacacacaccccacacacacacacacatactactatcactacgactcgatgagagaagtgaactacgagtcacagatgcatacagatgatgatagatagctagcatgatagcatgcagaagaactgatatctacacgtacgtactgactgacgtactgactgactgactgactgacgtacgtacgtactgacgtactgacgtacgtacgtactgactgacgtacgtacgtacgtacgtactactgacgtacgtacactgacgtacgtacgtactactacacgtactgactacgtacgtacgtacgtactcatctgactgactgactcgtactactacgtactactacgtactgactgactactgactgactgatcatagtatggcgcgcgcgcgacgtacgtcagtcagctgtcagctgtacgatgctgctagcagtcagactgactacgtacgtcagatgatgatgctagccatgctagtacgatgactgactacgatcgactgatcgatcgatcgtcagctactgcatcgatcacgtgacgtatcatcgcatgctacgtagctacgtacgtacgactcgatgcatcgactgatgctacgtagctagctgatcgatcagtacgtacgtagctagctgcagcatcgatgcatagtcgatcgcatgcatgcatagtcgactacgtacgtagctgactgactgactgactacgatcgactgactacgggtgactaaaaaaaaacacacaccccacacacacacacacatactactatcactacgactcgatgagagaagtgaactacgagtcacagatgcatacagatgatgatagatagctagcatgatagcatgcagaagaactgatatctacacgtacgtactgactgacgtactgactgactgactgactgacgtacgtacgtactgacgtactgacgtacgtacgtactgactgacgtacgtacgtacgtacgtactactgacgtacgtacactgacgtacgtacgtactactacacgtactgactacgtacgtacgtacgtactcatctgactgactgactcgtactactacgtactactacgtactgactgactactgactgactgatcatagtatggcgcgcgcgcgacgtacgtcagtcagctgtcagctgtacgatgctgctagcagtcagactgactacgtacgtcagatgatgatgctagccatgctagtacgatgactgactacgatcgactgatcgatcgatcgtcagctactgcatcgatcacgtgacgtatcatcgcatgctacgtagctacgtacgtacgactcgatgcatcgactgatgctacgtagctagctgatcgatcagtacgtacgtagctagctgcagcatcgatgcatagtcgatcgcatgcatgcatagtcgactacgtacgtagctgactgactgactgactacgatcgactgactacgggtgactaaaaaaaaacacacaccccacacacacacacacatactactatcactacgactcgatgagagaagtgaactacgagtcacagatgcatacagatgatgatagatagctagcatgatagcatgcagaagaactgatatctacacgtacgtactgactgacgtactgactgactgactgactgacgtacgtacgtactgacgtactgacgtacgtacgtactgactgacgtacgtacgtacgtacgtactactgacgtacgtacactgacgtacgtacgtactactacacgtactgactacgtacgtacgtacgtactcatctgactgactgactcgtactactacgtactactacgtactgactgactactgactgactgatcatagtatggcgcgcgcgcgacgtacgtcagtcagctgtcagctgtacgatgctgctagcagtcagactgactacgtacgtcagatgatgatgctagccatgctagtacgatgactgactacgatcgactgatcgatcgatcgtcagctactgcatcgatcacgtgacgtatcatcgcatgctacgtagctacgtacgtacgactcgatgcatcgactgatgctacgtagctagctgatcgatcagtacgtacgtagctagctgcagcatcgatgcatagtcgatcgcatgcatgcatagtcgactacgtacgtagctgactgactgactgactacgatcgactgactacgggtgactaaaaaaaaacacacaccccacacacacacacacatactactatcactacgactcgatgagagaagtgaactacgagtcacagatgcatacagatgatgatagatagctagcatgatagcatgcagaagaactgatatctacacgtacgtactgactgacgtactgactgactgactgactgacgtacgtacgtactgacgtactgacgtacgtacgtactgactgacgtacgtacgtacgtacgtactactgacgtacgtacactgacgtacgtacgtactactacacgtactgactacgtacgtacgtacgtactcatctgactgactgactcgtactactacgtactactacgtactgactgactactgactgactgatcatagtatggcgcgcgcgcgacgtacgtcagtcagctgtcagctgtacgatgctgctagcagtcagactgactacgtacgtcagatgatgatgctagccatgctagtacgatgactgactacgatcgactgatcgatcgatcgtcagctactgcatcgatcacgtgacgtatcatcgcatgctacgtagctacgtacgtacgactcgatgcatcgactgatgctacgtagctagctgatcgatcagtacgtacgtagctagctgcagcatcgatgcatagtcgatcgcatgcatgcatagtcgactacgtacgtagctgactgactgactgactacgatcgactgactacgggtgactaaaaaaaaacacacaccccacacacacacacacatactactatcactacgactcgatgagagaagtgaactacgagtcacagatgcatacagatgatgatagatagctagcatgatagcatgcagaagaactgatatctacacgtacgtactgactgacgtactgactgactgactgactgacgtacgtacgtactgacgtactgacgtacgtacgtactgactgacgtacgtacgtacgtacgtactactgacgtacgtacactgacgtacgtacgtactactacacgtactgactacgtacgtacgtacgtactcatctgactgactgactcgtactactacgtactactacgtactgactgactactgactgactgatcatagtatggcgcgcgcgcgacgtacgtcagtcagctgtcagctgtacgatgctgctagcagtcagactgactacgtacgtcagatgatgatgctagccatgctagtacgatgactgactacgatcgactgatcgatcgatcgtcagctactgcatcgatcacgtgacgtatcatcgcatgctacgtagctacgtacgtacgactcgatgcatcgactgatgctacgtagctagctgatcgatcagtacgtacgtagctagctgcagcatcgatgcatagtcgatcgcatgcatgcatagtcgactacgtacgtagctgactgactgactgactacgatcgactgactacgggtgactaaaaaaaaacacacaccccacacacacacacacatactactatcactacgactcgatgagagaagtgaactacgagtcacagatgcatacagatgatgatagatagctagcatgatagcatgcagaagaactgatatctacacgtacgtactgactgacgtactgactgactgactgactgacgtacgtacgtactgacgtactgacgtacgtacgtactgactgacgtacgtacgtacgtacgtactactgacgtacgtacactgacgtacgtacgtactactacacgtactgactacgtacgtacgtacgtactcatctgactgactgactcgtactactacgtactactacgtactgactgactactgactgactgatcatagtatggcgcgcgcgcgacgtacgtcagtcagctgtcagctgtacgatgctgctagcagtcagactgactacgtacgtcagatgatgatgctagccatgctagtacgatgactgactacgatcgactgatcgatcgatcgtcagctactgcatcgatcacgtgacgtatcatcgcatgctacgtagctacgtacgtacgactcgatgcatcgactgatgctacgtagctagctgatcgatcagtacgtacgtagctagctgcagcatcgatgcatagtcgatcgcatgcatgcatagtcgactacgtacgtagctgactgactgactgactacgatcgactgactacgggtgactaaaaaaaaacacacaccccacacacacacacacatactactatcactacgactcgatgagagaagtgaactacgagtcacagatgcatacagatgatgatagatagctagcatgatagcatgcagaagaactgatatctacacgtacgtactgactgacgtactgactgactgactgactgacgtacgtacgtactgacgtactgacgtacgtacgtactgactgacgtacgtacgtacgtacgtactactgacgtacgtacactgacgtacgtacgtactactacacgtactgactacgtacgtacgtacgtactcatctgactgactgactcgtactactacgtactactacgtactgactgactactgactgactgatcatagtatggcgcgcgcgcgacgtacgtcagtcagctgtcagctgtacgatgctgctagcagtcagactgactacgtacgtcagatgatgatgctagccatgctagtacgatgactgactacgatcgactgatcgatcgatcgtcagctactgcatcgatcacgtgacgtatcatcgcatgctacgtagctacgtacgtacgactcgatgcatcgactgatgctacgtagctagctgatcgatcagtacgtacgtagctagctgcagcatcgatgcatagtcgatcgcatgcatgcatagtcgactacgtacgtagctgactgactgactgactacgatcgactgactacgggtgactaaaaaaaaacacacaccccacacacacacacacatactactatcactacgactcgatgagagaagtgaactacgagtcacagatgcatacagatgatgatagatagctagcatgatagcatgcagaagaactgatatctacacgtacgtactgactgacgtactgactgactgactgactgacgtacgtacgtactgacgtactgacgtacgtacgtactgactgacgtacgtacgtacgtacgtactactgacgtacgtacactgacgtacgtacgtactactacacgtactgactacgtacgtacgtacgtactcatctgactgactgactcgtactactacgtactactacgtactgactgactactgactgactgatcatagtatggcgcgcgcgcgacgtacgtcagtcagctgtcagctgtacgatgctgctagcagtcagactgactacgtacgtcagatgatgatgctagccatgctagtacgatgactgactacgatcgactgatcgatcgatcgtcagctactgcatcgatcacgtgacgtatcatcgcatgctacgtagctacgtacgtacgactcgatgcatcgactgatgctacgtagctagctgatcgatcagtacgtacgtagctagctgcagcatcgatgcatagtcgatcgcatgcatgcatagtcgactacgtacgtagctgactgactgactgactacgatcgactgactacgggtgactaaaaaaaaacacacaccccacacacacacacacatactactatcactacgactcgatgagagaagtgaactacgagtcacagatgcatacagatgatgatagatagctagcatgatagcatgcagaagaactgatatctacacgtacgtactgactgacgtactgactgactgactgactgacgtacgtacgtactgacgtactgacgtacgtacgtactgactgacgtacgtacgtacgtacgtactactgacgtacgtacactgacgtacgtacgtactactacacgtactgactacgtacgtacgtacgtactcatctgactgactgactcgtactactacgtactactacgtactgactgactactgactgactgatcatagtatggcgcgcgcgcgacgtacgtcagtcagctgtcagctgtacgatgctgctagcagtcagactgactacgtacgtcagatgatgatgctagccatgctagtacgatgactgactacgatcgactgatcgatcgatcgtcagctactgcatcgatcacgtgacgtatcatcgcatgctacgtagctacgtacgtacgactcgatgcatcgactgatgctacgtagctagctgatcgatcagtacgtacgtagctagctgcagcatcgatgcatagtcgatcgcatgcatgcatagtcgactacgtacgtagctgactgactgactgactacgatcgactgactacgggtgactaaaaaaaaacacacaccccacacacacacacacatactactatcactacgactcgatgagagaagtgaactacgagtcacagatgcatacagatgatgatagatagctagcatgatagcatgcagaagaactgatatctacacgtacgtactgactgacgtactgactgactgactgactgacgtacgtacgtactgacgtactgacgtacgtacgtactgactgacgtacgtacgtacgtacgtactactgacgtacgtacactgacgtacgtacgtactactacacgtactgactacgtacgtacgtacgtactcatctgactgactgactcgtactactacgtactactacgtactgactgactactgactgactgatcatagtatggcgcgcgcgcgacgtacgtcagtcagctgtcagctgtacgatgctgctagcagtcagactgactacgtacgtcagatgatgatgctagccatgctagtacgatgactgactacgatcgactgatcgatcgatcgtcagctactgcatcgatcacgtgacgtatcatcgcatgctacgtagctacgtacgtacgactcgatgcatcgactgatgctacgtagctagctgatcgatcagtacgtacgtagctagctgcagcatcgatgcatagtcgatcgcatgcatgcatagtcgactacgtacgtagctgactgactgactgactacgatcgactgactacgggtgactaaaaaaaaacacacaccccacacacacacacacatactactatcactacgactcgatgagagaagtgaactacgagtcacagatgcatacagatgatgatagatagctagcatgatagcatgcagaagaactgatatctacacgtacgtactgactgacgtactgactgactgactgactgacgtacgtacgtactgacgtactgacgtacgtacgtactgactgacgtacgtacgtacgtacgtactactgacgtacgtacactgacgtacgtacgtactactacacgtactgactacgtacgtacgtacgtactcatctgactgactgactcgtactactacgtactactacgtactgactgactactgactgactgatcatagtatggcgcgcgcgcgacgtacgtcagtcagctgtcagctgtacgatgctgctagcagtcagactgactacgtacgtcagatgatgatgctagccatgctagtacgatgactgactacgatcgactgatcgatcgatcgtcagctactgcatcgatcacgtgacgtatcatcgcatgctacgtagctacgtacgtacgactcgatgcatcgactgatgctacgtagctagctgatcgatcagtacgtacgtagctagctgcagcatcgatgcatagtcgatcgcatgcatgcatagtcgactacgtacgtagctgactgactgactgactacgatcgactgactacgggtgactaaaaaaaaacacacaccccacacacacacacacatactactatcactacgactcgatgagagaagtgaactacgagtcacagatgcatacagatgatgatagatagctagcatgatagcatgcagaagaactgatatctacacgtacgtactgactgacgtactgactgactgactgactgacgtacgtacgtactgacgtactgacgtacgtacgtactgactgacgtacgtacgtacgtacgtactactgacgtacgtacactgacgtacgtacgtactactacacgtactgactacgtacgtacgtacgtactcatctgactgactgactcgtactactacgtactactacgtactgactgactactgactgactgatcatagtatggcgcgcgcgcgacgtacgtcagtcagctgtcagctgtacgatgctgctagcagtcagactgactacgtacgtcagatgatgatgctagccatgctagtacgatgactgactacgatcgactgatcgatcgatcgtcagctactgcatcgatcacgtgacgtatcatcgcatgctacgtagctacgtacgtacgactcgatgcatcgactgatgctacgtagctagctgatcgatcagtacgtacgtagctagctgcagcatcgatgcatagtcgatcgcatgcatgcatagtcgactacgtacgtagctgactgactgactgactacgatcgactgactacgggtgactaaaaaaaaacacacaccccacacacacacacacatactactatcactacgactcgatgagagaagtgaactacgagtcacagatgcatacagatgatgatagatagctagcatgatagcatgcagaagaactgatatctacacgtacgtactgactgacgtactgactgactgactgactgacgtacgtacgtactgacgtactgacgtacgtacgtactgactgacgtacgtacgtacgtacgtactactgacgtacgtacactgacgtacgtacgtactactacacgtactgactacgtacgtacgtacgtactcatctgactgactgactcgtactactacgtactactacgtactgactgactactgactgactgatcatagtatggcgcgcgcgcgacgtacgtcagtcagctgtcagctgtacgatgctgctagcagtcagactgactacgtacgtcagatgatgatgctagccatgctagtacgatgactgactacgatcgactgatcgatcgatcgtcagctactgcatcgatcacgtgacgtatcatcgcatgctacgtagctacgtacgtacgactcgatgcatcgactgatgctacgtagctagctgatcgatcagtacgtacgtagctagctgcagcatcgatgcatagtcgatcgcatgcatgcatagtcgactacgtacgtagctgactgactgactgactacgatcgactgactacgggtgactaaaaaaaaacacacaccccacacacacacacacatactactatcactacgactcgatgagagaagtgaactacgagtcacagatgcatacagatgatgatagatagctagcatgatagcatgcagaagaactgatatctacacgtacgtactgactgacgtactgactgactgactgactgacgtacgtacgtactgacgtactgacgtacgtacgtactgactgacgtacgtacgtacgtacgtactactgacgtacgtacactgacgtacgtacgtactactacacgtactgactacgtacgtacgtacgtactcatctgactgactgactcgtactactacgtactactacgtactgactgactactgactgactgatcatagtatggcgcgcgcgcgacgtacgtcagtcagctgtcagctgtacgatgctgctagcagtcagactgactacgtacgtcagatgatgatgctagccatgctagtacgatgactgactacgatcgactgatcgatcgatcgtcagctactgcatcgatcacgtgacgtatcatcgcatgctacgtagctacgtacgtacgactcgatgcatcgactgatgctacgtagctagctgatcgatcagtacgtacgtagctagctgcagcatcgatgcatagtcgatcgcatgcatgcatagtcgactacgtacgtagctgactgactgactgactacgatcgactgactacgggtgactaaaaaaaaacacacaccccacacacacacacacatactactatcactacgactcgatgagagaagtgaactacgagtcacagatgcatacagatgatgatagatagctagcatgatagcatgcagaagaactgatatctacacgtacgtactgactgacgtactgactgactgactgactgacgtacgtacgtactgacgtactgacgtacgtacgtactgactgacgtacgtacgtacgtacgtactactgacgtacgtacactgacgtacgtacgtactactacacgtactgactacgtacgtacgtacgtactcatctgactgactgactcgtactactacgtactactacgtactgactgactactgactgactgatcatagtatggcgcgcgcgcgacgtacgtcagtcagctgtcagctgtacgatgctgctagcagtcagactgactacgtacgtcagatgatgatgctagccatgctagtacgatgactgactacgatcgactgatcgatcgatcgtcagctactgcatcgatcacgtgacgtatcatcgcatgctacgtagctacgtacgtacgactcgatgcatcgactgatgctacgtagctagctgatcgatcagtacgtacgtagctagctgcagcatcgatgcatagtcgatcgcatgcatgcatagtcgactacgtacgtagctgactgactgactgactacgatcgactgactacgggtgactaaaaaaaaacacacaccccacacacacacacacatactactatcactacgactcgatgagagaagtgaactacgagtcacagatgcatacagatgatgatagatagctagcatgatagcatgcagaagaactgatatctacacgtacgtactgactgacgtactgactgactgactgactgacgtacgtacgtactgacgtactgacgtacgtacgtactgactgacgtacgtacgtacgtacgtactactgacgtacgtacactgacgtacgtacgtactactacacgtactgactacgtacgtacgtacgtactcatctgactgactgactcgtactactacgtactactacgtactgactgactactgactgactgatcatagtatggcgcgcgcgcgacgtacgtcagtcagctgtcagctgtacgatgctgctagcagtcagactgactacgtacgtcagatgatgatgctagccatgctagtacgatgactgactacgatcgactgatcgatcgatcgtcagctactgcatcgatcacgtgacgtatcatcgcatgctacgtagctacgtacgtacgactcgatgcatcgactgatgctacgtagctagctgatcgatcagtacgtacgtagctagctgcagcatcgatgcatagtcgatcgcatgcatgcatagtcgactacgtacgtagctgactgactgactgactacgatcgactgactacgggtgactaaaaaaaaacacacaccccacacacacacacacatactactatcactacgactcgatgagagaagtgaactacgagtcacagatgcatacagatgatgatagatagctagcatgatagcatgcagaagaactgatatctacacgtacgtactgactgacgtactgactgactgactgactgacgtacgtacgtactgacgtactgacgtacgtacgtactgactgacgtacgtacgtacgtacgtactactgacgtacgtacactgacgtacgtacgtactactacacgtactgactacgtacgtacgtacgtactcatctgactgactgactcgtactactacgtactactacgtactgactgactactgactgactgatcatagtatggcgcgcgcgcgacgtacgtcagtcagctgtcagctgtacgatgctgctagcagtcagactgactacgtacgtcagatgatgatgctagccatgctagtacgatgactgactacgatcgactgatcgatcgatcgtcagctactgcatcgatcacgtgacgtatcatcgcatgctacgtagctacgtacgtacgactcgatgcatcgactgatgctacgtagctagctgatcgatcagtacgtacgtagctagctgcagcatcgatgcatagtcgatcgcatgcatgcatagtcgactacgtacgtagctgactgactgactgactacgatcgactgactacgggtgactaaaaaaaaacacacaccccacacacacacacacatactactatcactacgactcgatgagagaagtgaactacgagtcacagatgcatacagatgatgatagatagctagcatgatagcatgcagaagaactgatatctacacgtacgtactgactgacgtactgactgactgactgactgacgtacgtacgtactgacgtactgacgtacgtacgtactgactgacgtacgtacgtacgtacgtactactgacgtacgtacactgacgtacgtacgtactactacacgtactgactacgtacgtacgtacgtactcatctgactgactgactcgtactactacgtactactacgtactgactgactactgactgactgatcatagtatggcgcgcgcgcgacgtacgtcagtcagctgtcagctgtacgatgctgctagcagtcagactgactacgtacgtcagatgatgatgctagccatgctagtacgatgactgactacgatcgactgatcgatcgatcgtcagctactgcatcgatcacgtgacgtatcatcgcatgctacgtagctacgtacgtacgactcgatgcatcgactgatgctacgtagctagctgatcgatcagtacgtacgtagctagctgcagcatcgatgcatagtcgatcgcatgcatgcatagtcgactacgtacgtagctgactgactgactgactacgatcgactgactacgggtgactaaaaaaaaacacacaccccacacacacacacacatactactatcactacgactcgatgagagaagtgaactacgagtcacagatgcatacagatgatgatagatagctagcatgatagcatgcagaagaactgatatctacacgtacgtactgactgacgtactgactgactgactgactgacgtacgtacgtactgacgtactgacgtacgtacgtactgactgacgtacgtacgtacgtacgtactactgacgtacgtacactgacgtacgtacgtactactacacgtactgactacgtacgtacgtacgtactcatctgactgactgactcgtactactacgtactactacgtactgactgactactgactgactgatcatagtatggcgcgcgcgcgacgtacgtcagtcagctgtcagctgtacgatgctgctagcagtcagactgactacgtacgtcagatgatgatgctagccatgctagtacgatgactgactacgatcgactgatcgatcgatcgtcagctactgcatcgatcacgtgacgtatcatcgcatgctacgtagctacgtacgtacgactcgatgcatcgactgatgctacgtagctagctgatcgatcagtacgtacgtagctagctgcagcatcgatgcatagtcgatcgcatgcatgcatagtcgactacgtacgtagctgactgactgactgactacgatcgactgactacgggtgactaaaaaaaaacacacaccccacacacacacacacatactactatcactacgactcgatgagagaagtgaactacgagtcacagatgcatacagatgatgatagatagctagcatgatagcatgcagaagaactgatatctacacgtacgtactgactgacgtactgactgactgactgactgacgtacgtacgtactgacgtactgacgtacgtacgtactgactgacgtacgtacgtacgtacgtactactgacgtacgtacactgacgtacgtacgtactactacacgtactgactacgtacgtacgtacgtactcatctgactgactgactcgtactactacgtactactacgtactgactgactactgactgactgatcatagtatggcgcgcgcgcgacgtacgtcagtcagctgtcagctgtacgatgctgctagcagtcagactgactacgtacgtcagatgatgatgctagccatgctagtacgatgactgactacgatcgactgatcgatcgatcgtcagctactgcatcgatcacgtgacgtatcatcgcatgctacgtagctacgtacgtacgactcgatgcatcgactgatgctacgtagctagctgatcgatcagtacgtacgtagctagctgcagcatcgatgcatagtcgatcgcatgcatgcatagtcgactacgtacgtagctgactgactgactgactacgatcgactgactacgggtgactaaaaaaaaacacacaccccacacacacacacacatactactatcactacgactcgatgagagaagtgaactacgagtcacagatgcatacagatgatgatagatagctagcatgatagcatgcagaagaactgatatctacacgtacgtactgactgacgtactgactgactgactgactgacgtacgtacgtactgacgtactgacgtacgtacgtactgactgacgtacgtacgtacgtacgtactactgacgtacgtacactgacgtacgtacgtactactacacgtactgactacgtacgtacgtacgtactcatctgactgactgactcgtactactacgtactactacgtactgactgactactgactgactgatcatagtatggcgcgcgcgcgacgtacgtcagtcagctgtcagctgtacgatgctgctagcagtcagactgactacgtacgtcagatgatgatgctagccatgctagtacgatgactgactacgatcgactgatcgatcgatcgtcagctactgcatcgatcacgtgacgtatcatcgcatgctacgtagctacgtacgtacgactcgatgcatcgactgatgctacgtagctagctgatcgatcagtacgtacgtagctagctgcagcatcgatgcatagtcgatcgcatgcatgcatagtcgactacgtacgtagctgactgactgactgactacgatcgactgactacgggtgactaaaaaaaaacacacaccccacacacacacacacatactactatcactacgactcgatgagagaagtgaactacgagtcacagatgcatacagatgatgatagatagctagcatgatagcatgcagaagaactgatatctacacgtacgtactgactgacgtactgactgactgactgactgacgtacgtacgtactgacgtactgacgtacgtacgtactgactgacgtacgtacgtacgtacgtactactgacgtacgtacactgacgtacgtacgtactactacacgtactgactacgtacgtacgtacgtactcatctgactgactgactcgtactactacgtactactacgtactgactgactactgactgactgatcatagtatggcgcgcgcgcgacgtacgtcagtcagctgtcagctgtacgatgctgctagcagtcagactgactacgtacgtcagatgatgatgctagccatgctagtacgatgactgactacgatcgactgatcgatcgatcgtcagctactgcatcgatcacgtgacgtatcatcgcatgctacgtagctacgtacgtacgactcgatgcatcgactgatgctacgtagctagctgatcgatcagtacgtacgtagctagctgcagcatcgatgcatagtcgatcgcatgcatgcatagtcgactacgtacgtagctgactgactgactgactacgatcgactgactacgggtgactaaaaaaaaacacacaccccacacacacacacacatactactatcactacgactcgatgagagaagtgaactacgagtcacagatgcatacagatgatgatagatagctagcatgatagcatgcagaagaactgatatctacacgtacgtactgactgacgtactgactgactgactgactgacgtacgtacgtactgacgtactgacgtacgtacgtactgactgacgtacgtacgtacgtacgtactactgacgtacgtacactgacgtacgtacgtactactacacgtactgactacgtacgtacgtacgtactcatctgactgactgactcgtactactacgtactactacgtactgactgactactgactgactgatcatagtatggcgcgcgcgcgacgtacgtcagtcagctgtcagctgtacgatgctgctagcagtcagactgactacgtacgtcagatgatgatgctagccatgctagtacgatgactgactacgatcg'.upper()
alpha = 0.3
time = 5
matrix = mutate.build_transition_matrix(alpha)
matrix = np.linalg.matrix_power(matrix, time)

def test_mutate(threads):

    node = mutate.PhylogeneticNode(dna)

    new_node = mutate.mutate_module(matrix, node, threads)

    return