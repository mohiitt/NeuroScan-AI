import math
def sigmoid(x):
    if x < 0.0:
        z = math.exp(x)
        return z / (1.0 + z)
    return 1.0 / (1.0 + math.exp(-x))
def score(input):
    if input[4] < 0.036548793:
        if input[52] < 0.31374943:
            var0 = 0.3277122
        else:
            var0 = 0.019845616
    else:
        if input[83] < -0.7245787:
            if input[57] < -0.8382639:
                if input[1] < 1.1594853:
                    var0 = 0.23668817
                else:
                    var0 = -0.043007255
            else:
                if input[60] < -0.9892713:
                    var0 = -0.09691583
                else:
                    if input[21] < -0.606188:
                        var0 = -0.026454223
                    else:
                        var0 = 0.11244529
        else:
            if input[36] < -0.82217366:
                if input[3] < 0.8355525:
                    var0 = -0.09214668
                else:
                    var0 = 0.04708581
            else:
                var0 = -0.13206603
    if input[4] < 0.036548793:
        if input[52] < 0.31374943:
            var1 = 0.26080325
        else:
            var1 = 0.018680394
    else:
        if input[83] < -0.7245787:
            if input[57] < -0.8382639:
                if input[1] < 1.1594853:
                    var1 = 0.20401983
                else:
                    var1 = -0.040934913
            else:
                if input[45] < 0.0074217888:
                    if input[63] < 0.26598772:
                        var1 = -0.091242224
                    else:
                        var1 = -0.02363552
                else:
                    var1 = 0.07549428
        else:
            if input[36] < -0.82217366:
                if input[32] < -0.20194909:
                    var1 = 0.04660268
                else:
                    var1 = -0.090184994
            else:
                var1 = -0.12756686
    if input[4] < 0.36450014:
        if input[52] < 0.5918866:
            if input[36] < 0.012460859:
                if input[9] < -0.41791216:
                    var2 = 0.23357287
                else:
                    var2 = 0.050316717
            else:
                if input[21] < -0.38505968:
                    var2 = 0.14957513
                else:
                    var2 = -0.07806611
        else:
            var2 = -0.032348614
    else:
        if input[93] < -0.96132684:
            if input[0] < 1.0:
                if input[9] < -1.0993974:
                    var2 = -0.085026674
                else:
                    var2 = 0.073892266
            else:
                var2 = 0.1649483
        else:
            if input[16] < -0.63303024:
                if input[3] < 0.8355525:
                    var2 = -0.095671624
                else:
                    var2 = 0.08984503
            else:
                var2 = -0.12434182
    if input[4] < 0.36450014:
        if input[52] < 0.5918866:
            if input[4] < 0.036548793:
                if input[84] < 0.85176814:
                    var3 = 0.20254655
                else:
                    var3 = 0.07270183
            else:
                if input[36] < -0.62603456:
                    var3 = 0.132864
                else:
                    var3 = -0.07219272
        else:
            var3 = -0.030813325
    else:
        if input[93] < -0.96132684:
            if input[0] < 1.0:
                if input[1] < 1.0793126:
                    var3 = 0.07247087
                else:
                    var3 = -0.08302113
            else:
                var3 = 0.1490325
        else:
            if input[16] < -0.63303024:
                if input[3] < 0.8355525:
                    var3 = -0.092346765
                else:
                    var3 = 0.082655706
            else:
                var3 = -0.12091316
    if input[4] < 0.36450014:
        if input[57] < 0.28285939:
            if input[36] < 0.3136248:
                if input[84] < 0.9710933:
                    if input[63] < 1.2762903:
                        var4 = 0.1911066
                    else:
                        var4 = 0.042852707
                else:
                    var4 = 0.047309037
            else:
                if input[29] < -1.123201:
                    var4 = 0.090915225
                else:
                    var4 = -0.035422634
        else:
            if input[45] < 0.429332:
                var4 = -0.06799639
            else:
                var4 = 0.06260086
    else:
        if input[51] < 0.21894191:
            if input[36] < 1.950204:
                var4 = -0.118160956
            else:
                var4 = -0.017903334
        else:
            if input[10] < 0.12062784:
                if input[68] < 0.2791295:
                    var4 = -0.09343787
                else:
                    var4 = 0.042258613
            else:
                if input[21] < -0.07450446:
                    var4 = 0.15334748
                else:
                    var4 = 0.00989057
    if input[4] < 0.36450014:
        if input[57] < 0.28285939:
            if input[92] < 0.28605735:
                if input[1] < 1.2797443:
                    var5 = 0.17528668
                else:
                    if input[2] < -0.06765037:
                        var5 = 0.13003479
                    else:
                        var5 = -0.05050963
            else:
                var5 = 0.024290865
        else:
            if input[21] < -0.6305772:
                var5 = 0.061731774
            else:
                var5 = -0.06728314
    else:
        if input[51] < 0.21894191:
            if input[20] < 0.7689075:
                var5 = -0.11536461
            else:
                var5 = -0.014974415
        else:
            if input[10] < 0.12062784:
                if input[0] < 1.0:
                    var5 = -0.09098212
                else:
                    var5 = 0.0421972
            else:
                if input[81] < 0.43672574:
                    var5 = 0.14090098
                else:
                    var5 = 0.0079755
    if input[4] < 0.36450014:
        if input[4] < -0.6193539:
            var6 = 0.16205984
        else:
            if input[36] < -0.3158287:
                if input[90] < 0.4738795:
                    if input[20] < 0.37651366:
                        var6 = 0.0591347
                    else:
                        var6 = -0.038234
                else:
                    if input[21] < -1.240306:
                        var6 = 0.037403934
                    else:
                        var6 = 0.15100919
            else:
                if input[17] < -0.56245625:
                    var6 = 0.0139472755
                else:
                    var6 = -0.08695685
    else:
        if input[93] < -0.96132684:
            if input[0] < 1.0:
                if input[1] < 1.0793126:
                    var6 = 0.062261607
                else:
                    var6 = -0.07759309
            else:
                var6 = 0.12832892
        else:
            if input[16] < -0.63303024:
                if input[3] < 0.8355525:
                    var6 = -0.083798185
                else:
                    var6 = 0.07281154
            else:
                var6 = -0.11326661
    if input[4] < 0.36450014:
        if input[34] < -0.02259957:
            var7 = -0.021126766
        else:
            if input[52] < 0.31374943:
                if input[4] < 0.036548793:
                    if input[16] < -1.9254552:
                        var7 = 0.058198065
                    else:
                        var7 = 0.15363722
                else:
                    if input[36] < -0.71088904:
                        var7 = 0.108131945
                    else:
                        var7 = -0.04011026
            else:
                var7 = -0.0026464742
    else:
        if input[51] < 0.21894191:
            if input[41] < 1.7081107:
                var7 = -0.11121289
            else:
                var7 = -0.013706485
        else:
            if input[10] < 0.12062784:
                if input[68] < 0.2791295:
                    var7 = -0.08749836
                else:
                    var7 = 0.04007304
            else:
                if input[21] < -0.07450446:
                    var7 = 0.12662964
                else:
                    var7 = 0.0057353405
    if input[9] < -0.41791216:
        if input[4] < 0.036548793:
            if input[84] < 0.85176814:
                var8 = 0.14042063
            else:
                var8 = 0.04197475
        else:
            if input[57] < -0.8382639:
                if input[1] < 1.119399:
                    var8 = 0.1418827
                else:
                    if input[57] < -1.1510123:
                        var8 = -0.07582694
                    else:
                        var8 = 0.061941504
            else:
                if input[24] < -0.14414816:
                    if input[82] < 1.2829299:
                        var8 = -0.09594052
                    else:
                        var8 = 0.011065274
                else:
                    var8 = 0.05016424
    else:
        if input[37] < -0.040436927:
            if input[84] < -0.8586772:
                var8 = 0.08624337
            else:
                var8 = -0.03308987
        else:
            var8 = -0.109466925
    if input[1] < 0.39784485:
        var9 = -0.10694539
    else:
        if input[4] < 0.036548793:
            if input[84] < 0.85176814:
                if input[68] < 1.5256269:
                    var9 = 0.1390155
                else:
                    var9 = 0.0469966
            else:
                if input[24] < -1.1336836:
                    var9 = 0.0902442
                else:
                    var9 = -0.04811396
        else:
            if input[57] < -0.8382639:
                if input[1] < 1.119399:
                    var9 = 0.13256931
                else:
                    if input[57] < -1.1510123:
                        var9 = -0.073302105
                    else:
                        var9 = 0.058390923
            else:
                if input[25] < -0.31037796:
                    var9 = 0.042328235
                else:
                    if input[70] < -0.03614602:
                        if input[84] < 0.034826774:
                            var9 = -0.09854211
                        else:
                            var9 = -0.017097468
                    else:
                        if input[47] < 0.42030632:
                            var9 = -0.06091102
                        else:
                            var9 = 0.07194452
    if input[9] < -0.41791216:
        if input[4] < 0.036548793:
            if input[9] < -0.6334947:
                if input[21] < -0.16067947:
                    var10 = 0.13328236
                else:
                    var10 = 0.036708158
            else:
                var10 = 0.016793288
        else:
            if input[57] < -0.8382639:
                if input[1] < 1.1594853:
                    if input[30] < 0.8098884:
                        var10 = 0.033585954
                    else:
                        var10 = 0.12433882
                else:
                    var10 = -0.037555043
            else:
                if input[24] < -0.14414816:
                    if input[82] < 1.2829299:
                        var10 = -0.09068551
                    else:
                        var10 = 0.012989312
                else:
                    var10 = 0.0472501
    else:
        if input[37] < -0.040436927:
            if input[56] < -0.15023446:
                var10 = -0.016330207
            else:
                var10 = 0.062069964
        else:
            var10 = -0.10609271
    if input[1] < 0.39784485:
        var11 = -0.103712
    else:
        if input[4] < 0.036548793:
            if input[84] < 0.85176814:
                if input[68] < 1.5256269:
                    var11 = 0.12780496
                else:
                    var11 = 0.03889704
            else:
                if input[4] < -0.94730526:
                    var11 = 0.081528135
                else:
                    var11 = -0.04807751
        else:
            if input[57] < -0.8382639:
                if input[1] < 1.119399:
                    var11 = 0.11914443
                else:
                    if input[57] < -1.1510123:
                        var11 = -0.070469305
                    else:
                        var11 = 0.05349282
            else:
                if input[25] < -0.31037796:
                    var11 = 0.04064421
                else:
                    if input[70] < -0.03614602:
                        if input[84] < -0.010719777:
                            var11 = -0.0936571
                        else:
                            var11 = -0.018479288
                    else:
                        var11 = 0.009663326
    if input[89] < -0.003371345:
        if input[4] < 0.036548793:
            var12 = 0.02043533
        else:
            var12 = -0.10288501
    else:
        if input[4] < 0.036548793:
            if input[52] < 0.27959225:
                if input[21] < -0.16067947:
                    var12 = 0.12350283
                else:
                    var12 = 0.031104928
            else:
                var12 = 0.0015191649
        else:
            if input[52] < -0.7987993:
                if input[26] < -0.25551373:
                    if input[26] < -0.90902543:
                        var12 = 0.03680694
                    else:
                        var12 = 0.11027553
                else:
                    var12 = -0.030789036
            else:
                if input[24] < -0.13104174:
                    if input[82] < 1.293698:
                        var12 = -0.09325637
                    else:
                        var12 = 0.023687292
                else:
                    var12 = 0.062055793
    if input[9] < -0.41791216:
        if input[4] < 0.036548793:
            if input[71] < 1.4768785:
                if input[84] < 0.85176814:
                    var13 = 0.11943289
                else:
                    var13 = 0.016197234
            else:
                var13 = 0.01760572
        else:
            if input[63] < 0.6637337:
                if input[30] < 1.5148337:
                    if input[3] < 1.9914001:
                        if input[45] < 0.16161104:
                            var13 = 0.113952436
                        else:
                            var13 = 0.008339175
                    else:
                        var13 = -0.02878724
                else:
                    var13 = -0.04533933
            else:
                if input[26] < -0.83344924:
                    var13 = 0.0053567155
                else:
                    var13 = -0.07574104
    else:
        if input[37] < -0.040436927:
            var13 = 0.026577571
        else:
            var13 = -0.101961054
    if input[1] < 0.39784485:
        var14 = -0.09957401
    else:
        if input[4] < -0.6193539:
            var14 = 0.11536324
        else:
            if input[92] < -0.36371195:
                if input[2] < 1.9741608:
                    if input[37] < -1.9550747:
                        var14 = -0.012789153
                    else:
                        if input[29] < -0.7316428:
                            var14 = 0.11255658
                        else:
                            var14 = 0.009947737
                else:
                    var14 = -0.02771237
            else:
                if input[29] < 0.49791333:
                    if input[84] < -0.7451552:
                        if input[4] < 0.36450014:
                            var14 = 0.057484545
                        else:
                            var14 = -0.036164872
                    else:
                        var14 = -0.092110716
                else:
                    var14 = 0.05360759
    if input[89] < -0.003371345:
        if input[16] < -0.87173146:
            var15 = 0.00050899177
        else:
            var15 = -0.09967249
    else:
        if input[4] < 0.036548793:
            if input[84] < 0.85176814:
                var15 = 0.10675763
            else:
                if input[30] < 0.84541434:
                    var15 = -0.048973452
                else:
                    var15 = 0.070448555
        else:
            if input[52] < -0.7987993:
                if input[1] < 1.1594853:
                    if input[63] < -0.25371522:
                        var15 = 0.005261415
                    else:
                        var15 = 0.106581986
                else:
                    var15 = -0.027263392
            else:
                if input[24] < -0.13104174:
                    if input[82] < 1.2893908:
                        var15 = -0.0882268
                    else:
                        var15 = 0.011325201
                else:
                    var15 = 0.05755936
    if input[1] < 0.39784485:
        var16 = -0.09699054
    else:
        if input[4] < -0.6193539:
            var16 = 0.10908141
        else:
            if input[57] < -0.8382639:
                if input[1] < 1.3198307:
                    if input[78] < -1.5205547:
                        var16 = 0.014062985
                    else:
                        var16 = 0.10681106
                else:
                    var16 = -0.048010778
            else:
                if input[63] < 0.5972118:
                    if input[55] < -1.1490554:
                        var16 = -0.06412961
                    else:
                        if input[51] < 0.21894191:
                            var16 = -0.017216474
                        else:
                            var16 = 0.07689991
                else:
                    var16 = -0.08294146
    if input[1] < 0.39784485:
        var17 = -0.095677786
    else:
        if input[4] < -0.6193539:
            var17 = 0.10580603
        else:
            if input[91] < 0.07042016:
                var17 = -0.07419428
            else:
                if input[1] < 1.3198307:
                    if input[26] < 0.08383814:
                        if input[4] < 0.6924515:
                            var17 = 0.08266234
                        else:
                            var17 = 0.0009809715
                    else:
                        if input[36] < -0.6399451:
                            var17 = 0.021897543
                        else:
                            var17 = -0.06297823
                else:
                    if input[2] < 0.9532552:
                        var17 = 0.0012657464
                    else:
                        var17 = -0.07664832
    if input[1] < 0.39784485:
        var18 = -0.09437641
    else:
        if input[4] < -0.6193539:
            var18 = 0.10278108
        else:
            if input[57] < -0.8382639:
                if input[1] < 1.2797443:
                    if input[76] < 0.6911823:
                        var18 = 0.10165906
                    else:
                        var18 = 0.022934055
                else:
                    var18 = -0.03181863
            else:
                if input[63] < 0.5972118:
                    if input[55] < -1.1490554:
                        var18 = -0.060444515
                    else:
                        if input[55] < -0.3040605:
                            var18 = 0.062591635
                        else:
                            var18 = -0.031738
                else:
                    var18 = -0.08009473
    if input[9] < -0.41791216:
        if input[4] < 0.036548793:
            if input[94] < 0.2874454:
                var19 = 0.09807395
            else:
                if input[65] < -1.6013218:
                    var19 = -0.030266762
                else:
                    var19 = 0.0607584
        else:
            if input[63] < 0.6637337:
                if input[63] < 0.30202046:
                    if input[81] < -0.24578215:
                        if input[84] < -0.11288539:
                            var19 = 0.05058072
                        else:
                            var19 = -0.036711607
                    else:
                        var19 = -0.06390553
                else:
                    var19 = 0.08274197
            else:
                if input[9] < -0.8224383:
                    var19 = -0.06610422
                else:
                    var19 = -0.0035321687
    else:
        if input[37] < -0.040436927:
            var19 = 0.020261398
        else:
            var19 = -0.09503537
    if input[89] < -0.003371345:
        if input[16] < -0.87173146:
            var20 = -0.00055925985
        else:
            var20 = -0.0934697
    else:
        if input[4] < 0.036548793:
            if input[44] < 0.47726133:
                var20 = -0.0035789732
            else:
                if input[1] < 1.3198307:
                    var20 = 0.099542774
                else:
                    var20 = 0.028987644
        else:
            if input[24] < -0.13104174:
                if input[30] < 0.802226:
                    var20 = -0.08304944
                else:
                    if input[26] < -0.90902543:
                        if input[57] < -1.2570287:
                            var20 = 0.04127449
                        else:
                            var20 = -0.06912521
                    else:
                        var20 = 0.07406946
            else:
                if input[16] < -0.71248996:
                    var20 = 0.07982778
                else:
                    var20 = 0.008344788
    if input[1] < 0.39784485:
        var21 = -0.09061101
    else:
        if input[4] < -0.6193539:
            var21 = 0.09636431
        else:
            if input[57] < -0.8382639:
                if input[1] < 1.3198307:
                    if input[78] < -1.5205547:
                        var21 = 0.0076634646
                    else:
                        var21 = 0.09220091
                else:
                    var21 = -0.0427656
            else:
                if input[63] < 0.5972118:
                    if input[55] < -1.1490554:
                        var21 = -0.059088655
                    else:
                        if input[83] < -0.9124685:
                            var21 = 0.07912271
                        else:
                            var21 = -0.0017497039
                else:
                    var21 = -0.07598108
    if input[1] < 0.39784485:
        var22 = -0.089283414
    else:
        if input[4] < -0.6193539:
            var22 = 0.09389273
        else:
            if input[57] < -0.8382639:
                if input[1] < 1.2797443:
                    if input[29] < -0.6852046:
                        var22 = 0.090801194
                    else:
                        var22 = 0.020620888
                else:
                    var22 = -0.029137982
            else:
                if input[63] < 0.5972118:
                    if input[55] < -1.1490554:
                        var22 = -0.056183416
                    else:
                        if input[26] < -0.95940953:
                            var22 = -0.028962811
                        else:
                            var22 = 0.054172453
                else:
                    var22 = -0.07378995
    if input[89] < -0.003371345:
        if input[16] < -0.87173146:
            var23 = -0.00075337355
        else:
            var23 = -0.089762785
    else:
        if input[4] < 0.036548793:
            if input[84] < 0.85176814:
                var23 = 0.08856912
            else:
                var23 = -0.0030126076
        else:
            if input[24] < -0.13104174:
                if input[30] < 0.802226:
                    var23 = -0.07983335
                else:
                    if input[26] < -0.90902543:
                        if input[57] < -1.2570287:
                            var23 = 0.03448872
                        else:
                            var23 = -0.065443724
                    else:
                        var23 = 0.06689918
            else:
                if input[84] < -0.7331312:
                    var23 = 0.072915904
                else:
                    var23 = 0.007823898
    if input[9] < -0.41791216:
        if input[4] < 0.036548793:
            if input[84] < 0.85176814:
                var24 = 0.0864992
            else:
                var24 = 0.0051517216
        else:
            if input[2] < 1.9741608:
                if input[3] < 1.9914001:
                    if input[81] < 0.9518611:
                        if input[91] < 1.2215756:
                            var24 = 0.084756814
                        else:
                            var24 = 0.007366147
                    else:
                        var24 = -0.02222225
                else:
                    var24 = -0.041397396
            else:
                var24 = -0.05222096
    else:
        if input[37] < -0.040436927:
            var24 = 0.015620822
        else:
            var24 = -0.08953577
    if input[1] < 0.39784485:
        var25 = -0.08542783
    else:
        if input[4] < -0.6193539:
            var25 = 0.08880709
        else:
            if input[57] < -0.8382639:
                if input[1] < 1.3198307:
                    if input[81] < 0.86445546:
                        var25 = 0.08367353
                    else:
                        var25 = 0.0065226103
                else:
                    var25 = -0.040665437
            else:
                if input[77] < 0.9147948:
                    if input[64] < -0.23335221:
                        var25 = 0.023124626
                    else:
                        if input[52] < -0.15957172:
                            var25 = -0.0028400556
                        else:
                            var25 = -0.08698245
                else:
                    if input[57] < -0.3187836:
                        var25 = -0.032673072
                    else:
                        if input[77] < 1.0818424:
                            var25 = 0.06701638
                        else:
                            var25 = 0.00716791
    if input[89] < -0.003371345:
        if input[16] < -0.6416867:
            var26 = -0.0061542722
        else:
            var26 = -0.08573716
    else:
        if input[4] < -0.6193539:
            var26 = 0.082773685
        else:
            if input[1] < 1.3198307:
                if input[26] < 0.08383814:
                    if input[78] < -0.91171443:
                        if input[91] < 1.3513398:
                            var26 = 0.086808585
                        else:
                            var26 = 0.018178923
                    else:
                        if input[44] < 0.3356796:
                            var26 = 0.060682435
                        else:
                            var26 = -0.023798294
                else:
                    var26 = -0.03366986
            else:
                var26 = -0.04554407
    if input[1] < 0.39784485:
        var27 = -0.08273458
    else:
        if input[4] < -0.6193539:
            var27 = 0.084968306
        else:
            if input[64] < 1.1866517:
                if input[1] < 1.119399:
                    if input[57] < -0.8382639:
                        var27 = 0.07049396
                    else:
                        if input[63] < 0.5972118:
                            var27 = 0.010852781
                        else:
                            var27 = -0.063108645
                else:
                    if input[30] < 0.84541434:
                        var27 = -0.07192304
                    else:
                        var27 = -0.00058792124
            else:
                if input[30] < 1.5622015:
                    var27 = 0.0664614
                else:
                    var27 = -0.0041579576
    if input[89] < -0.003371345:
        if input[16] < -0.5388651:
            var28 = -0.008547417
        else:
            var28 = -0.08269253
    else:
        if input[4] < 0.36450014:
            if input[50] < -0.13146491:
                if input[3] < -0.32029513:
                    var28 = 0.0057523646
                else:
                    if input[5] < 0.116201185:
                        var28 = 0.094528496
                    else:
                        var28 = 0.019767547
            else:
                var28 = -0.013195189
        else:
            if input[32] < -0.48448133:
                var28 = -0.052116483
            else:
                if input[94] < -0.64875823:
                    var28 = -0.029891236
                else:
                    if input[37] < -0.19808549:
                        var28 = 0.07461854
                    else:
                        var28 = -0.0014135643
    if input[9] < -0.41791216:
        if input[4] < 0.036548793:
            if input[84] < 0.85176814:
                var29 = 0.07966466
            else:
                var29 = 0.0001889379
        else:
            if input[2] < 1.9741608:
                if input[3] < 1.9914001:
                    if input[81] < 0.9518611:
                        if input[91] < 1.2215756:
                            var29 = 0.07399333
                        else:
                            var29 = 0.007254322
                    else:
                        var29 = -0.01933372
                else:
                    var29 = -0.040196173
            else:
                var29 = -0.050249983
    else:
        if input[37] < -0.040436927:
            var29 = 0.013473968
        else:
            var29 = -0.08364974
    if input[1] < 0.39784485:
        var30 = -0.07858562
    else:
        if input[4] < -0.6193539:
            var30 = 0.08042407
        else:
            if input[57] < -0.8382639:
                if input[1] < 1.2797443:
                    var30 = 0.06848644
                else:
                    var30 = -0.029572962
            else:
                if input[29] < 0.20450853:
                    if input[19] < -0.65615714:
                        if input[21] < -0.693989:
                            var30 = -0.023650674
                        else:
                            var30 = 0.04569354
                    else:
                        var30 = -0.069647565
                else:
                    var30 = 0.02853117
    if input[91] < 0.13755225:
        if input[4] < 0.36450014:
            var31 = 0.004190286
        else:
            var31 = -0.08012238
    else:
        if input[2] < 1.9741608:
            if input[29] < -1.1400876:
                if input[92] < -0.68714964:
                    if input[34] < 1.7951193:
                        var31 = 0.08162097
                    else:
                        var31 = 0.022394082
                else:
                    var31 = 0.018790433
            else:
                if input[24] < -0.13104174:
                    if input[73] < -1.0555146:
                        var31 = 0.02116774
                    else:
                        var31 = -0.058962382
                else:
                    if input[84] < -0.7331312:
                        var31 = 0.07929947
                    else:
                        var31 = 0.009559329
        else:
            var31 = -0.029715478
    if input[89] < -0.003371345:
        if input[16] < -0.40743476:
            var32 = -0.012463216
        else:
            var32 = -0.07661925
    else:
        if input[4] < 0.036548793:
            if input[84] < 0.85176814:
                var32 = 0.07501998
            else:
                var32 = -0.009140606
        else:
            if input[24] < -0.13104174:
                if input[30] < 0.802226:
                    var32 = -0.071581736
                else:
                    if input[52] < -0.83295643:
                        var32 = 0.046199623
                    else:
                        var32 = -0.029498369
            else:
                if input[45] < -0.09177564:
                    var32 = 0.007796717
                else:
                    var32 = 0.061385542
    if input[9] < -0.41791216:
        if input[4] < 0.036548793:
            if input[84] < 0.85176814:
                var33 = 0.07403161
            else:
                var33 = -0.0010678814
        else:
            if input[1] < 1.119399:
                if input[57] < -0.8382639:
                    var33 = 0.068734065
                else:
                    if input[32] < 0.112682045:
                        var33 = -0.044216335
                    else:
                        var33 = 0.027929971
            else:
                if input[57] < -0.9787356:
                    var33 = -0.060778845
                else:
                    var33 = 0.0017825727
    else:
        if input[37] < -0.040436927:
            var33 = 0.011225341
        else:
            var33 = -0.07875279
    if input[91] < 0.13755225:
        if input[4] < 0.36450014:
            var34 = 0.0026926817
        else:
            var34 = -0.07605495
    else:
        if input[1] < 1.3198307:
            if input[51] < 0.60182714:
                if input[24] < -0.13104174:
                    if input[52] < -0.5889765:
                        var34 = 0.011167274
                    else:
                        var34 = -0.061569232
                else:
                    var34 = 0.049798977
            else:
                if input[37] < -1.6273111:
                    var34 = 0.01204774
                else:
                    if input[50] < -1.2454844:
                        var34 = 0.025015712
                    else:
                        var34 = 0.08111448
        else:
            var34 = -0.028803295
    if input[4] < -0.6193539:
        var35 = 0.07494509
    else:
        if input[91] < 0.13755225:
            var35 = -0.075895675
        else:
            if input[1] < 1.3198307:
                if input[32] < -0.6191195:
                    if input[45] < 0.042420145:
                        var35 = 0.019814933
                    else:
                        var35 = -0.051265944
                else:
                    if input[3] < 1.9914001:
                        if input[26] < -0.90902543:
                            var35 = 0.006494091
                        else:
                            var35 = 0.07320934
                    else:
                        var35 = -0.011657146
            else:
                var35 = -0.041017853
    if input[4] < -0.6193539:
        var36 = 0.07304685
    else:
        if input[91] < 0.13755225:
            var36 = -0.073849745
        else:
            if input[24] < -0.13104174:
                if input[29] < -0.8857331:
                    if input[92] < -0.68714964:
                        if input[56] < 1.335786:
                            var36 = 0.00089706
                        else:
                            var36 = 0.061756045
                    else:
                        var36 = -0.01605678
                else:
                    var36 = -0.057538092
            else:
                if input[84] < -0.916191:
                    var36 = 0.06743657
                else:
                    var36 = 0.006797751
    if input[4] < 0.36450014:
        if input[36] < -0.30678684:
            if input[55] < -1.1730609:
                var37 = 0.0014644796
            else:
                var37 = 0.07609879
        else:
            if input[51] < 0.60182714:
                var37 = -0.049239423
            else:
                var37 = 0.028379017
    else:
        if input[14] < -0.3099374:
            if input[10] < -0.046851356:
                if input[0] < 1.0:
                    var37 = -0.06392166
                else:
                    var37 = 0.020831326
            else:
                if input[3] < 0.8355525:
                    var37 = 0.0071687284
                else:
                    var37 = 0.050581425
        else:
            var37 = -0.0749431
    if input[4] < -0.6193539:
        var38 = 0.07008832
    else:
        if input[91] < 0.13755225:
            var38 = -0.070555024
        else:
            if input[1] < 1.3198307:
                if input[32] < -0.6191195:
                    if input[50] < -1.2269174:
                        var38 = 0.022255966
                    else:
                        var38 = -0.04303504
                else:
                    if input[45] < -0.2984558:
                        if input[37] < -0.48039845:
                            var38 = 0.036535922
                        else:
                            var38 = -0.035949994
                    else:
                        var38 = 0.06675879
            else:
                var38 = -0.038806193
    if input[4] < -0.6193539:
        var39 = 0.068294466
    else:
        if input[91] < 0.07042016:
            var39 = -0.071959995
        else:
            if input[29] < 0.20450853:
                if input[92] < -0.36371195:
                    if input[1] < 1.119399:
                        if input[57] < -0.8382639:
                            var39 = 0.06503889
                        else:
                            var39 = -0.00033131172
                    else:
                        if input[55] < -0.3184638:
                            var39 = 0.033414282
                        else:
                            var39 = -0.05445498
                else:
                    if input[77] < 0.9381701:
                        var39 = -0.06478287
                    else:
                        var39 = -0.0033241585
            else:
                var39 = 0.052617002
    if input[4] < 0.036548793:
        if input[44] < 0.47726133:
            var40 = -0.00766629
        else:
            var40 = 0.063157015
    else:
        if input[91] < 0.13755225:
            var40 = -0.06802684
        else:
            if input[24] < -0.13104174:
                if input[82] < 1.2893908:
                    if input[36] < -1.1476811:
                        var40 = -0.002770887
                    else:
                        var40 = -0.06863666
                else:
                    var40 = 0.025813669
            else:
                var40 = 0.038542
    if input[4] < -0.6193539:
        var41 = 0.06542664
    else:
        if input[91] < 0.07042016:
            var41 = -0.06892695
        else:
            if input[1] < 1.3198307:
                if input[36] < -0.27827016:
                    if input[57] < -0.8382639:
                        var41 = 0.06875602
                    else:
                        if input[45] < -0.09992477:
                            var41 = -0.04163123
                        else:
                            var41 = 0.03449354
                else:
                    var41 = -0.030827984
            else:
                var41 = -0.037457015
    if input[4] < 0.036548793:
        if input[18] < -0.09547384:
            if input[41] < -1.0107946:
                var42 = 0.017272241
            else:
                var42 = 0.06877791
        else:
            var42 = -0.01105573
    else:
        if input[91] < 0.13755225:
            var42 = -0.06485234
        else:
            if input[24] < -0.13104174:
                if input[82] < 1.2893908:
                    if input[36] < -1.1476811:
                        var42 = -0.0043367646
                    else:
                        var42 = -0.06629463
                else:
                    var42 = 0.023359412
            else:
                var42 = 0.035914283
    if input[4] < -0.6193539:
        var43 = 0.06268815
    else:
        if input[9] < -0.6264246:
            if input[1] < 1.3198307:
                if input[3] < 1.9914001:
                    if input[2] < 0.9532552:
                        var43 = 0.06717533
                    else:
                        if input[82] < 1.277187:
                            var43 = -0.018008972
                        else:
                            var43 = 0.03132059
                else:
                    var43 = -0.0197643
            else:
                var43 = -0.035552364
        else:
            if input[36] < -0.8145228:
                var43 = 0.014458339
            else:
                var43 = -0.072903834
    if input[4] < 0.36450014:
        if input[36] < -0.30678684:
            if input[63] < -0.11235602:
                var44 = 0.071921
            else:
                var44 = 0.015164492
        else:
            var44 = -0.015110944
    else:
        if input[16] < -0.3329317:
            if input[51] < 0.21894191:
                var44 = -0.031021876
            else:
                if input[55] < -0.4048837:
                    var44 = -0.0076774172
                else:
                    var44 = 0.04371011
        else:
            var44 = -0.06279146
    var45 = var0 + var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8 + var9 + var10 + var11 + var12 + var13 + var14 + var15 + var16 + var17 + var18 + var19 + var20 + var21 + var22 + var23 + var24 + var25 + var26 + var27 + var28 + var29 + var30 + var31 + var32 + var33 + var34 + var35 + var36 + var37 + var38 + var39 + var40 + var41 + var42 + var43 + var44
    if input[64] < 1.2090547:
        if input[16] < -0.63303024:
            if input[81] < 0.86445546:
                if input[1] < 0.8788809:
                    var46 = 0.053642552
                else:
                    var46 = 0.00779986
            else:
                var46 = -0.026603168
        else:
            if input[68] < 0.61083776:
                var46 = -0.0658454
            else:
                var46 = 0.0049444875
    else:
        if input[4] < 0.36450014:
            var46 = 0.0604402
        else:
            var46 = 0.0027633384
    if input[4] < -0.6193539:
        var47 = 0.05949862
    else:
        if input[91] < 0.13755225:
            var47 = -0.059470892
        else:
            if input[24] < -0.13104174:
                if input[29] < -0.8857331:
                    if input[92] < -0.68714964:
                        if input[1] < 1.119399:
                            var47 = 0.051562425
                        else:
                            var47 = 0.005156743
                    else:
                        var47 = -0.01505279
                else:
                    var47 = -0.052409988
            else:
                var47 = 0.037591208
    if input[4] < 0.036548793:
        if input[34] < 0.6153096:
            var48 = -0.0039497977
        else:
            var48 = 0.061811544
    else:
        if input[71] < 0.71800625:
            if input[71] < -0.46649972:
                if input[55] < -0.71695566:
                    var48 = 0.023102118
                else:
                    var48 = -0.026637211
            else:
                if input[92] < -0.6119088:
                    var48 = -0.014695312
                else:
                    var48 = -0.06558459
        else:
            if input[73] < -1.0345362:
                var48 = 0.035267852
            else:
                var48 = -0.009196173
    if input[4] < 0.036548793:
        if input[34] < 0.6153096:
            var49 = -0.0037162944
        else:
            var49 = 0.059712853
    else:
        if input[57] < -0.8382639:
            if input[83] < -1.3469186:
                var49 = -0.011117631
            else:
                var49 = 0.03347376
        else:
            if input[92] < 0.4633932:
                var49 = -0.057406634
            else:
                var49 = 0.0027121278
    if input[4] < -0.6193539:
        var50 = 0.056160357
    else:
        if input[9] < -0.6264246:
            if input[1] < 1.3198307:
                if input[51] < 0.3899392:
                    var50 = -0.005589947
                else:
                    if input[37] < -1.3462968:
                        var50 = -0.00079477904
                    else:
                        var50 = 0.06183819
            else:
                var50 = -0.034428447
        else:
            if input[36] < -0.7595761:
                var50 = 0.008363375
            else:
                var50 = -0.066016786
    if input[4] < 0.36450014:
        if input[36] < -0.30678684:
            if input[63] < -0.11235602:
                var51 = 0.06598621
            else:
                var51 = 0.013053422
        else:
            var51 = -0.015553946
    else:
        if input[78] < -0.91171443:
            if input[84] < -0.0021682365:
                var51 = -0.007031098
            else:
                var51 = 0.028751153
        else:
            if input[51] < 0.21894191:
                var51 = -0.06418672
            else:
                var51 = -0.005804242
    if input[4] < -0.6193539:
        var52 = 0.054175507
    else:
        if input[91] < 0.07042016:
            var52 = -0.056812137
        else:
            if input[29] < 0.20450853:
                if input[92] < -0.36371195:
                    if input[1] < 1.119399:
                        if input[52] < -0.7987993:
                            var52 = 0.051404465
                        else:
                            var52 = 0.0023678888
                    else:
                        var52 = -0.014167544
                else:
                    if input[84] < -0.45441335:
                        var52 = -0.01078493
                    else:
                        var52 = -0.05413298
            else:
                var52 = 0.044169925
    if input[64] < 1.2090547:
        if input[16] < -0.63303024:
            if input[2] < 0.9532552:
                if input[56] < 0.20291393:
                    var53 = 0.0024619559
                else:
                    var53 = 0.05338045
            else:
                var53 = -0.02608873
        else:
            if input[68] < 0.61083776:
                var53 = -0.059572317
            else:
                var53 = 0.0070165703
    else:
        if input[4] < 0.036548793:
            var53 = 0.054518025
        else:
            var53 = 0.0076588863
    if input[4] < 0.036548793:
        if input[34] < 0.6153096:
            var54 = -0.003734547
        else:
            var54 = 0.054843742
    else:
        if input[71] < 0.71800625:
            if input[71] < -0.46649972:
                var54 = 0.00037863143
            else:
                var54 = -0.05020557
        else:
            var54 = 0.017479317
    if input[64] < 1.2090547:
        if input[16] < -0.63303024:
            if input[81] < 0.86445546:
                if input[34] < 0.35305804:
                    var55 = 0.044965982
                else:
                    var55 = 0.010116036
            else:
                var55 = -0.026795825
        else:
            if input[68] < 0.5149534:
                var55 = -0.05901241
            else:
                var55 = 0.0053836456
    else:
        if input[20] < 1.4066137:
            var55 = 0.050411906
        else:
            var55 = 0.0077114045
    if input[4] < 0.36450014:
        if input[36] < -0.30678684:
            if input[63] < -0.11235602:
                var56 = 0.06189173
            else:
                var56 = 0.011718342
        else:
            var56 = -0.015019387
    else:
        if input[92] < -0.8276184:
            var56 = 0.019891841
        else:
            if input[16] < -0.71248996:
                var56 = -0.0029976172
            else:
                var56 = -0.055335473
    if input[77] < 0.7352044:
        if input[84] < -0.7331312:
            var57 = 0.023687698
        else:
            if input[16] < -0.71248996:
                var57 = 0.001121074
            else:
                var57 = -0.06317785
    else:
        if input[18] < -0.17029257:
            if input[30] < 1.3260587:
                if input[77] < 1.1040773:
                    var57 = 0.061947834
                else:
                    var57 = 0.016322445
            else:
                var57 = -0.001861649
        else:
            var57 = -0.017641826
    if input[4] < 0.036548793:
        if input[52] < -0.14005332:
            var58 = 0.05089733
        else:
            var58 = -0.00600279
    else:
        if input[71] < 0.71800625:
            if input[71] < -0.46649972:
                var58 = 0.00011637834
            else:
                var58 = -0.047083043
        else:
            var58 = 0.01705523
    if input[64] < 1.2090547:
        if input[92] < -0.35707724:
            if input[58] < 0.28227726:
                var59 = 0.030631645
            else:
                var59 = -0.019482808
        else:
            if input[29] < 0.25516835:
                var59 = -0.053081807
            else:
                var59 = 0.00469093
    else:
        if input[21] < -0.9638956:
            var59 = 0.006997641
        else:
            var59 = 0.04537928
    if input[51] < 0.60182714:
        if input[84] < -0.70001274:
            var60 = 0.018776285
        else:
            if input[16] < -0.71248996:
                var60 = -0.0031540114
            else:
                var60 = -0.06038676
    else:
        if input[1] < 1.2797443:
            if input[50] < -1.161933:
                var60 = 0.009447673
            else:
                var60 = 0.055970103
        else:
            var60 = -0.010937939
    if input[4] < 0.36450014:
        if input[36] < -0.30678684:
            if input[63] < -0.11235602:
                var61 = 0.057893097
            else:
                var61 = 0.010817568
        else:
            var61 = -0.013973
    else:
        if input[16] < -0.3329317:
            if input[68] < 0.6173164:
                var61 = 0.02590304
            else:
                var61 = -0.025137944
        else:
            var61 = -0.04895739
    if input[29] < -1.1400876:
        if input[52] < -0.77440125:
            var62 = 0.045846652
        else:
            var62 = -0.0020452512
    else:
        if input[84] < -0.70001274:
            var62 = 0.024951419
        else:
            if input[77] < 0.7352044:
                var62 = -0.05056885
            else:
                var62 = -0.00528034
    if input[4] < 0.036548793:
        if input[34] < 0.6153096:
            var63 = -0.0036985048
        else:
            var63 = 0.04938328
    else:
        if input[71] < 0.71800625:
            if input[71] < -0.46649972:
                var63 = 0.0006176898
            else:
                var63 = -0.044599682
        else:
            var63 = 0.015493976
    if input[4] < 0.036548793:
        if input[34] < 0.6153096:
            var64 = -0.0035009612
        else:
            var64 = 0.04770353
    else:
        if input[71] < 0.71800625:
            if input[71] < -0.46649972:
                var64 = 0.0005789363
            else:
                var64 = -0.04243964
        else:
            var64 = 0.014535203
    if input[29] < -1.1400876:
        if input[30] < 1.3497427:
            var65 = 0.048907064
        else:
            var65 = -0.0005286814
    else:
        if input[84] < -0.70001274:
            var65 = 0.023500072
        else:
            if input[77] < 0.71924084:
                var65 = -0.047574636
            else:
                var65 = -0.0059604025
    if input[4] < 0.036548793:
        if input[34] < 0.6153096:
            var66 = -0.0028478128
        else:
            var66 = 0.04598818
    else:
        if input[92] < -0.8246345:
            var66 = 0.013944203
        else:
            if input[92] < 0.47708073:
                var66 = -0.046283133
            else:
                var66 = 0.008518695
    if input[64] < 1.2090547:
        if input[1] < 1.119399:
            if input[9] < -0.43086022:
                if input[84] < -0.24516176:
                    var67 = 0.00406054
                else:
                    var67 = 0.04409348
            else:
                var67 = -0.029684905
        else:
            var67 = -0.03761017
    else:
        var67 = 0.030341718
    if input[4] < 0.036548793:
        if input[34] < 0.6153096:
            var68 = -0.0018940581
        else:
            var68 = 0.04424899
    else:
        if input[52] < -0.7987993:
            var68 = 0.013506574
        else:
            if input[92] < 0.47708073:
                var68 = -0.045676555
            else:
                var68 = 0.008005069
    if input[84] < -0.70001274:
        if input[4] < 0.36450014:
            var69 = 0.04035708
        else:
            var69 = -0.006430406
    else:
        if input[29] < -1.1622514:
            var69 = 0.028088272
        else:
            if input[1] < 0.8788809:
                var69 = -0.0093243765
            else:
                var69 = -0.0508591
    if input[4] < 0.036548793:
        if input[34] < 0.6153096:
            var70 = -0.0014624546
        else:
            var70 = 0.042490643
    else:
        if input[71] < 0.71800625:
            if input[69] < 0.72582036:
                if input[56] < 0.5106076:
                    var70 = -0.03253488
                else:
                    var70 = 0.030704511
            else:
                var70 = -0.047061756
        else:
            var70 = 0.014386067
    if input[84] < -0.70001274:
        if input[4] < 0.36450014:
            var71 = 0.038331956
        else:
            var71 = -0.0056430963
    else:
        if input[29] < -1.1622514:
            var71 = 0.025796106
        else:
            if input[1] < 0.8788809:
                var71 = -0.008175629
            else:
                var71 = -0.049213495
    if input[4] < 0.036548793:
        if input[92] < -0.36371195:
            var72 = 0.03867135
        else:
            var72 = 0.00014940013
    else:
        if input[71] < 0.71800625:
            if input[70] < -0.14057302:
                if input[92] < -0.85219806:
                    var72 = -0.0063564754
                else:
                    var72 = -0.04595298
            else:
                var72 = 0.0058766264
        else:
            var72 = 0.013495005
    if input[36] < -0.27827016:
        if input[4] < 0.36450014:
            var73 = 0.036732715
        else:
            if input[0] < 1.0:
                var73 = -0.028626624
            else:
                var73 = 0.022032456
    else:
        var73 = -0.023773067
    if input[64] < 1.2090547:
        if input[1] < 1.119399:
            if input[14] < -0.3099374:
                var74 = 0.03109835
            else:
                var74 = -0.024309043
        else:
            var74 = -0.035943497
    else:
        var74 = 0.027476033
    if input[52] < -0.77440125:
        if input[94] < -0.12998614:
            var75 = 0.040583197
        else:
            var75 = -0.008376518
    else:
        if input[77] < 0.9147948:
            if input[10] < 0.11324861:
                var75 = -0.0024932097
            else:
                var75 = -0.04066384
        else:
            var75 = 0.012274365
    if input[4] < 0.036548793:
        var76 = 0.024843749
    else:
        if input[71] < 0.71800625:
            if input[58] < 0.12359846:
                var76 = -0.04074016
            else:
                var76 = 0.00037292516
        else:
            var76 = 0.012607341
    if input[1] < 1.3198307:
        if input[36] < -0.27827016:
            if input[57] < -0.8382639:
                var77 = 0.055705108
            else:
                if input[45] < 0.012249189:
                    var77 = -0.028554758
                else:
                    var77 = 0.025593324
        else:
            var77 = -0.02428841
    else:
        var77 = -0.029101405
    if input[4] < 0.036548793:
        var78 = 0.023855787
    else:
        if input[52] < -0.7987993:
            var78 = 0.010735569
        else:
            if input[92] < 0.6912296:
                var78 = -0.040239643
            else:
                var78 = 0.013549546
    if input[84] < -0.70001274:
        if input[60] < -1.101354:
            var79 = -0.0069305487
        else:
            var79 = 0.03494302
    else:
        if input[29] < -1.1622514:
            var79 = 0.02267369
        else:
            if input[1] < 0.8788809:
                var79 = -0.0058889943
            else:
                var79 = -0.04740053
    if input[1] < 1.3198307:
        if input[9] < -0.6264246:
            if input[51] < 0.3899392:
                var80 = 0.0026928636
            else:
                var80 = 0.03664383
        else:
            var80 = -0.01921924
    else:
        var80 = -0.027800484
    if input[4] < 0.036548793:
        var81 = 0.023446476
    else:
        if input[71] < 0.71800625:
            if input[70] < -0.25453466:
                var81 = -0.035771083
            else:
                var81 = 0.005597717
        else:
            var81 = 0.011135346
    if input[84] < -0.70001274:
        if input[4] < 0.36450014:
            var82 = 0.034030624
        else:
            var82 = -0.0057082833
    else:
        if input[29] < -1.1622514:
            var82 = 0.021320147
        else:
            if input[16] < -0.71248996:
                var82 = -0.0045475005
            else:
                var82 = -0.045483053
    if input[1] < 1.119399:
        if input[14] < -0.3099374:
            if input[81] < -0.4652261:
                var83 = 0.004949813
            else:
                var83 = 0.04587658
        else:
            var83 = -0.021738825
    else:
        if input[30] < 0.84541434:
            var83 = -0.036433116
        else:
            var83 = 0.005516929
    if input[4] < 0.036548793:
        var84 = 0.022666171
    else:
        if input[24] < -0.13104174:
            if input[82] < 1.2893908:
                var84 = -0.04267561
            else:
                var84 = 0.0131197395
        else:
            var84 = 0.009584237
    if input[84] < -0.70001274:
        if input[60] < -1.101354:
            var85 = -0.007087638
        else:
            var85 = 0.032522205
    else:
        if input[29] < -1.1622514:
            var85 = 0.019629993
        else:
            if input[1] < 0.8788809:
                var85 = -0.0046360954
            else:
                var85 = -0.044698115
    if input[4] < 0.036548793:
        var86 = 0.021985853
    else:
        if input[57] < -0.8382639:
            var86 = 0.010125607
        else:
            if input[92] < 0.4633932:
                var86 = -0.040648602
            else:
                var86 = 0.008535431
    if input[63] < 0.68036425:
        if input[63] < 0.30202046:
            if input[77] < 0.91764545:
                var87 = -0.035516486
            else:
                var87 = 0.015839344
        else:
            var87 = 0.043733127
    else:
        var87 = -0.023511285
    if input[1] < 1.119399:
        if input[14] < -0.3099374:
            if input[10] < -0.049002714:
                var88 = 0.005484566
            else:
                var88 = 0.04553606
        else:
            var88 = -0.020682147
    else:
        if input[84] < -0.7451552:
            var88 = 0.004905186
        else:
            var88 = -0.031573005
    if input[4] < 0.036548793:
        var89 = 0.02176834
    else:
        if input[24] < -0.13104174:
            if input[92] < -0.8246345:
                var89 = 0.0072603696
            else:
                var89 = -0.041661564
        else:
            var89 = 0.009112596
    if input[84] < -0.70001274:
        if input[60] < -1.101354:
            var90 = -0.006879302
        else:
            var90 = 0.030767024
    else:
        if input[29] < -1.1622514:
            var90 = 0.018501647
        else:
            if input[16] < -0.71248996:
                var90 = -0.0042748232
            else:
                var90 = -0.041906003
    if input[4] < 0.036548793:
        var91 = 0.020825615
    else:
        if input[71] < 0.71800625:
            if input[70] < -0.25453466:
                var91 = -0.033943597
            else:
                var91 = 0.006069025
        else:
            var91 = 0.010890402
    if input[50] < -0.07576395:
        if input[1] < 1.119399:
            if input[47] < 0.100493535:
                var92 = 0.041197963
            else:
                var92 = -0.00036514085
        else:
            var92 = -0.01177249
    else:
        var92 = -0.021684814
    if input[84] < -0.70001274:
        if input[4] < 0.36450014:
            var93 = 0.030574992
        else:
            var93 = -0.00555247
    else:
        if input[29] < -1.1305889:
            var93 = 0.016844898
        else:
            if input[90] < 0.39847478:
                var93 = -0.0029039027
            else:
                var93 = -0.039555192
    if input[57] < -0.8382639:
        var94 = 0.018589417
    else:
        if input[92] < 0.6912296:
            if input[37] < -0.5993491:
                var94 = 0.0042793695
            else:
                var94 = -0.0401469
        else:
            var94 = 0.014882012
    if input[4] < 0.036548793:
        var95 = 0.020572117
    else:
        if input[24] < -0.13104174:
            if input[82] < 1.2829299:
                var95 = -0.03858019
            else:
                var95 = 0.008205501
        else:
            var95 = 0.00919097
    if input[36] < -0.27827016:
        if input[55] < -1.1586576:
            var96 = -0.019721858
        else:
            if input[4] < 0.36450014:
                var96 = 0.045701414
            else:
                var96 = -0.0012522689
    else:
        var96 = -0.020871824
    if input[1] < 1.119399:
        if input[14] < -0.3099374:
            if input[76] < -0.39315635:
                var97 = 0.004913955
            else:
                var97 = 0.04298694
        else:
            var97 = -0.02041401
    else:
        if input[29] < -1.1400876:
            var97 = 0.0038174314
        else:
            var97 = -0.02906323
    if input[4] < 0.036548793:
        var98 = 0.019834366
    else:
        if input[24] < -0.13104174:
            if input[92] < -0.8246345:
                var98 = 0.006688273
            else:
                var98 = -0.0391614
        else:
            var98 = 0.008954852
    if input[63] < 0.68036425:
        if input[63] < 0.30202046:
            if input[77] < 0.91764545:
                var99 = -0.03247032
            else:
                var99 = 0.014509954
        else:
            var99 = 0.039044894
    else:
        var99 = -0.021161053
    if input[84] < -0.70001274:
        if input[41] < -0.76539195:
            var100 = -0.0046989825
        else:
            var100 = 0.029235011
    else:
        if input[78] < -0.91171443:
            var100 = 0.008707366
        else:
            var100 = -0.030999253
    var101 = sigmoid(var45 + var46 + var47 + var48 + var49 + var50 + var51 + var52 + var53 + var54 + var55 + var56 + var57 + var58 + var59 + var60 + var61 + var62 + var63 + var64 + var65 + var66 + var67 + var68 + var69 + var70 + var71 + var72 + var73 + var74 + var75 + var76 + var77 + var78 + var79 + var80 + var81 + var82 + var83 + var84 + var85 + var86 + var87 + var88 + var89 + var90 + var91 + var92 + var93 + var94 + var95 + var96 + var97 + var98 + var99 + var100)
    return [1.0 - var101, var101]
