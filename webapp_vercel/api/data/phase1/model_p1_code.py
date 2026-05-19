import math
def sigmoid(x):
    if x < 0.0:
        z = math.exp(x)
        return z / (1.0 + z)
    return 1.0 / (1.0 + math.exp(-x))
def score(input):
    if input[4] < 0.036548793:
        if input[6] < -0.2620209:
            var0 = 0.31977466
        else:
            var0 = 0.06614545
    else:
        if input[6] < -0.19452065:
            if input[1] < 1.1594853:
                if input[3] < 1.9914001:
                    if input[2] < 1.9741608:
                        if input[6] < -0.9370233:
                            var0 = 0.23188563
                        else:
                            var0 = 0.036291085
                    else:
                        var0 = -0.0495319
                else:
                    var0 = -0.05519652
            else:
                if input[6] < -1.5951506:
                    var0 = 0.019845616
                else:
                    var0 = -0.09892731
        else:
            if input[1] < 0.75862193:
                var0 = -0.13185382
            else:
                var0 = -0.043007255
    if input[4] < 0.036548793:
        if input[6] < -0.2620209:
            var1 = 0.25517318
        else:
            var1 = 0.061510038
    else:
        if input[6] < -0.19452065:
            if input[1] < 1.3198307:
                if input[3] < 1.9914001:
                    if input[2] < 1.9741608:
                        if input[6] < -0.9370233:
                            var1 = 0.22575441
                        else:
                            var1 = 0.02253168
                    else:
                        var1 = -0.057865888
                else:
                    var1 = -0.06577105
            else:
                var1 = -0.08928984
        else:
            if input[1] < 0.75862193:
                var1 = -0.12735508
            else:
                var1 = -0.040934913
    if input[4] < 0.36450014:
        if input[4] < 0.036548793:
            if input[4] < -0.6193539:
                var2 = 0.23899594
            else:
                if input[6] < -0.7513976:
                    if input[1] < 1.3198307:
                        var2 = 0.19874066
                    else:
                        var2 = 0.04879136
                else:
                    var2 = -0.01594789
        else:
            if input[5] < -0.8091793:
                var2 = -0.024556985
            else:
                if input[1] < 1.0392263:
                    var2 = 0.12458885
                else:
                    var2 = -0.024236294
    else:
        if input[6] < -0.295771:
            if input[0] < 1.0:
                if input[6] < -0.565772:
                    if input[1] < 0.8788809:
                        var2 = 0.01092021
                    else:
                        var2 = -0.10504086
                else:
                    var2 = 0.092993885
            else:
                if input[1] < 0.91896725:
                    var2 = -0.00561976
                else:
                    var2 = 0.12376317
        else:
            var2 = -0.12403405
    if input[4] < 0.36450014:
        if input[4] < 0.036548793:
            if input[6] < -0.2620209:
                var3 = 0.19043034
            else:
                var3 = 0.04960663
        else:
            if input[5] < -0.8091793:
                var3 = -0.023410346
            else:
                if input[5] < 0.020472169:
                    var3 = 0.1296479
                else:
                    var3 = -0.010183706
    else:
        if input[6] < -0.295771:
            if input[1] < 1.3198307:
                if input[2] < 1.9741608:
                    if input[3] < 1.9914001:
                        if input[6] < -0.9370233:
                            var3 = 0.16511795
                        else:
                            var3 = 0.022270497
                    else:
                        var3 = -0.03705964
                else:
                    var3 = -0.047900755
            else:
                var3 = -0.08317693
        else:
            var3 = -0.12062802
    if input[4] < 0.36450014:
        if input[4] < -0.6193539:
            var4 = 0.18979363
        else:
            if input[6] < -0.7513976:
                if input[4] < 0.036548793:
                    if input[1] < 1.3198307:
                        var4 = 0.16131774
                    else:
                        var4 = 0.034739595
                else:
                    var4 = 0.038605712
            else:
                if input[2] < 0.9532552:
                    if input[1] < 0.8387946:
                        var4 = -0.023766616
                    else:
                        var4 = 0.05991119
                else:
                    var4 = -0.036487106
    else:
        if input[6] < -0.295771:
            if input[1] < 1.3198307:
                if input[2] < 1.9741608:
                    if input[3] < 1.9914001:
                        if input[6] < -0.9370233:
                            var4 = 0.15140896
                        else:
                            var4 = 0.020441655
                    else:
                        var4 = -0.035291757
                else:
                    var4 = -0.045615304
            else:
                var4 = -0.0803515
        else:
            var4 = -0.11764252
    if input[4] < 0.36450014:
        if input[4] < -0.6193539:
            var5 = 0.17287804
        else:
            if input[6] < -0.7513976:
                if input[4] < 0.036548793:
                    if input[1] < 1.3198307:
                        var5 = 0.14884569
                    else:
                        var5 = 0.032752454
                else:
                    var5 = 0.036002908
            else:
                if input[2] < 0.9532552:
                    if input[5] < -0.61772126:
                        var5 = -0.015583247
                    else:
                        var5 = 0.06607222
                else:
                    var5 = -0.034749914
    else:
        if input[6] < -0.295771:
            if input[6] < -0.565772:
                if input[0] < 1.0:
                    if input[1] < 0.8788809:
                        var5 = 0.012829825
                    else:
                        var5 = -0.09836556
                else:
                    if input[1] < 0.91896725:
                        var5 = -0.028530503
                    else:
                        var5 = 0.095120355
            else:
                var5 = 0.087968506
        else:
            var5 = -0.11500033
    if input[4] < 0.36450014:
        if input[4] < -0.6193539:
            var6 = 0.15977773
        else:
            if input[6] < -0.7513976:
                if input[4] < 0.036548793:
                    if input[1] < 1.3198307:
                        var6 = 0.13863516
                    else:
                        var6 = 0.030889576
                else:
                    var6 = 0.03359325
            else:
                if input[2] < 0.9532552:
                    if input[5] < -0.61772126:
                        var6 = -0.014675315
                    else:
                        var6 = 0.061915275
                else:
                    var6 = -0.03310247
    else:
        if input[6] < -0.295771:
            if input[6] < -0.565772:
                if input[0] < 1.0:
                    if input[1] < 0.8788809:
                        var6 = 0.012061487
                    else:
                        var6 = -0.09514325
                else:
                    if input[1] < 0.91896725:
                        var6 = -0.027201856
                    else:
                        var6 = 0.08809554
            else:
                var6 = 0.08025293
        else:
            var6 = -0.112639986
    if input[4] < 0.36450014:
        if input[4] < -0.6193539:
            var7 = 0.14931744
        else:
            if input[6] < -0.7513976:
                if input[2] < 1.9741608:
                    if input[6] < -1.3926499:
                        var7 = 0.037270606
                    else:
                        var7 = 0.1403704
                else:
                    var7 = 0.023413492
            else:
                if input[5] < -0.7772696:
                    var7 = 0.03438132
                else:
                    if input[4] < 0.036548793:
                        var7 = -0.049902234
                    else:
                        var7 = 0.02369507
    else:
        if input[6] < -0.295771:
            if input[1] < 1.3198307:
                if input[2] < 1.9741608:
                    if input[3] < 1.9914001:
                        if input[6] < -0.9370233:
                            var7 = 0.13007234
                        else:
                            var7 = 0.014969355
                    else:
                        var7 = -0.03403277
                else:
                    var7 = -0.038592745
            else:
                var7 = -0.07307719
        else:
            var7 = -0.110511854
    if input[4] < 0.36450014:
        if input[4] < -0.6193539:
            var8 = 0.14075626
        else:
            if input[6] < -0.7513976:
                if input[4] < 0.036548793:
                    if input[1] < 1.3198307:
                        var8 = 0.124916054
                    else:
                        var8 = 0.0248963
                else:
                    var8 = 0.026920069
            else:
                if input[2] < 0.9532552:
                    if input[1] < 0.8387946:
                        var8 = -0.023385188
                    else:
                        var8 = 0.05191649
                else:
                    var8 = -0.03158784
    else:
        if input[6] < -0.295771:
            if input[6] < -0.565772:
                if input[0] < 1.0:
                    if input[1] < 0.8788809:
                        var8 = 0.012525386
                    else:
                        var8 = -0.09101423
                else:
                    if input[1] < 1.0392263:
                        var8 = -0.017569093
                    else:
                        var8 = 0.08640105
            else:
                var8 = 0.07306136
        else:
            var8 = -0.10857525
    if input[4] < 0.36450014:
        if input[4] < -0.6193539:
            var9 = 0.13360302
        else:
            if input[6] < -0.5151468:
                if input[1] < 1.0793126:
                    var9 = 0.13204905
                else:
                    if input[2] < 0.9532552:
                        if input[1] < 1.1995716:
                            var9 = -0.012785802
                        else:
                            var9 = 0.10075966
                    else:
                        var9 = -0.04222423
            else:
                if input[1] < 0.8788809:
                    var9 = -0.074954234
                else:
                    var9 = 0.05864392
    else:
        if input[6] < -0.295771:
            if input[1] < 1.1594853:
                if input[6] < -0.582647:
                    if input[5] < 0.16087472:
                        if input[4] < 0.6924515:
                            var9 = 0.02145225
                        else:
                            var9 = -0.07888597
                    else:
                        if input[1] < 0.9590536:
                            var9 = 0.0058957823
                        else:
                            var9 = 0.06301596
                else:
                    var9 = 0.08417707
            else:
                var9 = -0.057780124
        else:
            var9 = -0.10679642
    if input[1] < 0.39784485:
        var10 = -0.10566461
    else:
        if input[4] < 0.36450014:
            if input[3] < -0.32029513:
                if input[5] < 0.20554827:
                    var10 = -0.05783176
                else:
                    var10 = 0.08941927
            else:
                if input[5] < 0.116201185:
                    if input[2] < -1.0885559:
                        if input[6] < -1.4264001:
                            var10 = 0.089149915
                        else:
                            var10 = -0.011899809
                    else:
                        if input[5] < -1.3899354:
                            var10 = 0.03786132
                        else:
                            var10 = 0.14489444
                else:
                    if input[4] < 0.036548793:
                        var10 = 0.10362697
                    else:
                        var10 = -0.038332786
        else:
            if input[0] < 1.0:
                if input[5] < -0.834707:
                    if input[6] < -0.7176475:
                        var10 = -0.033024453
                    else:
                        var10 = 0.058266044
                else:
                    if input[6] < -0.32952112:
                        var10 = -0.09159803
                    else:
                        var10 = -0.01725492
            else:
                if input[6] < -0.9370233:
                    var10 = 0.06835248
                else:
                    var10 = -0.030421624
    if input[1] < 0.39784485:
        var11 = -0.10403862
    else:
        if input[4] < 0.36450014:
            if input[3] < -0.32029513:
                if input[5] < 0.20554827:
                    var11 = -0.05504054
                else:
                    var11 = 0.08576489
            else:
                if input[5] < 0.116201185:
                    if input[2] < -1.0885559:
                        if input[6] < -1.4264001:
                            var11 = 0.085606545
                        else:
                            var11 = -0.0112825595
                    else:
                        if input[1] < 1.2797443:
                            var11 = 0.14158484
                        else:
                            var11 = 0.04587284
                else:
                    if input[4] < 0.036548793:
                        var11 = 0.099297136
                    else:
                        var11 = -0.036510374
        else:
            if input[6] < -0.295771:
                if input[1] < 0.75862193:
                    var11 = 0.093827
                else:
                    if input[3] < 1.9914001:
                        if input[1] < 1.3198307:
                            var11 = 0.0288288
                        else:
                            var11 = -0.059645306
                    else:
                        var11 = -0.075124726
            else:
                var11 = -0.071773194
    if input[1] < 0.39784485:
        var12 = -0.10250205
    else:
        if input[4] < 0.36450014:
            if input[3] < -0.32029513:
                if input[5] < 0.20554827:
                    var12 = -0.05240907
                else:
                    var12 = 0.08239281
            else:
                if input[3] < 0.8355525:
                    var12 = 0.12720263
                else:
                    if input[4] < 0.036548793:
                        if input[6] < -0.85264796:
                            var12 = 0.107220605
                        else:
                            var12 = 0.015195409
                    else:
                        var12 = -0.020689208
        else:
            if input[6] < -0.295771:
                if input[1] < 0.75862193:
                    var12 = 0.087043166
                else:
                    if input[3] < 1.9914001:
                        if input[1] < 1.3198307:
                            var12 = 0.026237193
                        else:
                            var12 = -0.05793534
                    else:
                        var12 = -0.072582684
            else:
                var12 = -0.069757245
    if input[1] < 0.39784485:
        var13 = -0.10103675
    else:
        if input[4] < 0.36450014:
            if input[4] < -0.6193539:
                var13 = 0.115555465
            else:
                if input[3] < -0.32029513:
                    var13 = -0.014443621
                else:
                    if input[3] < 0.8355525:
                        var13 = 0.11378854
                    else:
                        if input[4] < 0.036548793:
                            var13 = 0.043450207
                        else:
                            var13 = -0.019484172
        else:
            if input[0] < 1.0:
                if input[5] < -0.834707:
                    if input[6] < -0.7176475:
                        var13 = -0.031026015
                    else:
                        var13 = 0.056540072
                else:
                    var13 = -0.07512464
            else:
                if input[6] < -0.9370233:
                    if input[1] < 0.9590536:
                        var13 = 0.013266786
                    else:
                        var13 = 0.07569342
                else:
                    var13 = -0.03138907
    if input[1] < 0.39784485:
        var14 = -0.099627025
    else:
        if input[4] < 0.36450014:
            if input[4] < -0.6193539:
                var14 = 0.11168013
            else:
                if input[3] < -0.32029513:
                    var14 = -0.013563148
                else:
                    if input[3] < 0.8355525:
                        var14 = 0.10701796
                    else:
                        if input[5] < -0.5539019:
                            var14 = -0.02848461
                        else:
                            var14 = 0.038626846
        else:
            if input[6] < -0.295771:
                if input[1] < 0.75862193:
                    var14 = 0.08264124
                else:
                    if input[3] < 1.9914001:
                        if input[1] < 1.1594853:
                            var14 = 0.02626863
                        else:
                            var14 = -0.04174864
                    else:
                        var14 = -0.0691713
            else:
                var14 = -0.067745745
    if input[1] < 0.39784485:
        var15 = -0.09825922
    else:
        if input[4] < 0.036548793:
            if input[6] < -0.65014726:
                if input[5] < -1.1027483:
                    var15 = 0.026316613
                else:
                    var15 = 0.107104994
            else:
                if input[4] < -0.6193539:
                    var15 = 0.07617133
                else:
                    var15 = -0.029250933
        else:
            if input[3] < 1.9914001:
                if input[2] < 1.9741608:
                    if input[6] < -0.9370233:
                        var15 = 0.099822946
                    else:
                        if input[5] < 0.020472169:
                            var15 = 0.05640332
                        else:
                            var15 = -0.083006024
                else:
                    if input[6] < -0.85264796:
                        var15 = -0.06726266
                    else:
                        var15 = -0.012529373
            else:
                if input[1] < 0.79870826:
                    var15 = -0.01616169
                else:
                    var15 = -0.08297725
    if input[1] < 0.39784485:
        var16 = -0.09692144
    else:
        if input[4] < 0.036548793:
            if input[6] < -0.65014726:
                if input[5] < -1.1027483:
                    var16 = 0.025107993
                else:
                    var16 = 0.10298246
            else:
                if input[4] < -0.6193539:
                    var16 = 0.0735734
                else:
                    var16 = -0.02761644
        else:
            if input[3] < 1.9914001:
                if input[2] < 1.9741608:
                    if input[6] < -0.9370233:
                        var16 = 0.09284421
                    else:
                        if input[5] < 0.020472169:
                            var16 = 0.050988186
                        else:
                            var16 = -0.079950295
                else:
                    if input[6] < -0.85264796:
                        var16 = -0.06517368
                    else:
                        var16 = -0.01194087
            else:
                if input[5] < -0.16460393:
                    var16 = -0.015074054
                else:
                    var16 = -0.08059351
    if input[1] < 0.39784485:
        var17 = -0.09560328
    else:
        if input[4] < 0.36450014:
            if input[4] < -0.6193539:
                var17 = 0.10291784
            else:
                if input[3] < -0.32029513:
                    var17 = -0.020655103
                else:
                    if input[3] < 0.8355525:
                        var17 = 0.09635243
                    else:
                        if input[5] < -0.5539019:
                            var17 = -0.030984087
                        else:
                            var17 = 0.033800602
        else:
            if input[6] < -0.295771:
                if input[1] < 0.75862193:
                    var17 = 0.076248236
                else:
                    if input[5] < -0.834707:
                        if input[1] < 0.99913996:
                            var17 = 0.061819416
                        else:
                            var17 = -0.024702584
                    else:
                        if input[0] < 1.0:
                            var17 = -0.082939655
                        else:
                            var17 = 0.017929608
            else:
                var17 = -0.066364914
    if input[1] < 0.39784485:
        var18 = -0.09429573
    else:
        if input[4] < 0.036548793:
            if input[6] < -0.65014726:
                if input[5] < -1.1027483:
                    var18 = 0.020977505
                else:
                    if input[3] < -0.32029513:
                        var18 = 0.027647212
                    else:
                        var18 = 0.10440911
            else:
                if input[4] < -0.6193539:
                    var18 = 0.06779722
                else:
                    var18 = -0.028188873
        else:
            if input[3] < 1.9914001:
                if input[2] < 1.9741608:
                    if input[6] < -0.9370233:
                        var18 = 0.08625075
                    else:
                        if input[5] < 0.020472169:
                            var18 = 0.04543233
                        else:
                            var18 = -0.07734073
                else:
                    if input[6] < -0.85264796:
                        var18 = -0.06267818
                    else:
                        var18 = -0.010521545
            else:
                if input[1] < 0.79870826:
                    var18 = -0.012575242
                else:
                    var18 = -0.0780113
    if input[1] < 0.39784485:
        var19 = -0.092991024
    else:
        if input[4] < -0.6193539:
            var19 = 0.09801014
        else:
            if input[4] < 0.6924515:
                if input[6] < -0.48139668:
                    if input[1] < 0.8788809:
                        if input[6] < -0.9538984:
                            var19 = 0.031588968
                        else:
                            var19 = 0.13766383
                    else:
                        if input[3] < -0.32029513:
                            var19 = -0.056735225
                        else:
                            var19 = 0.028471235
                else:
                    if input[5] < -0.5347561:
                        var19 = -0.07394444
                    else:
                        var19 = 0.028003646
            else:
                if input[2] < 1.9741608:
                    if input[3] < 0.8355525:
                        var19 = 0.030422453
                    else:
                        var19 = -0.03538926
                else:
                    var19 = -0.07034549
    if input[1] < 0.39784485:
        var20 = -0.09168249
    else:
        if input[4] < 0.036548793:
            if input[4] < -0.6193539:
                var20 = 0.095486425
            else:
                if input[6] < -0.7513976:
                    if input[1] < 1.3198307:
                        var20 = 0.08457002
                    else:
                        var20 = -0.0017133007
                else:
                    var20 = -0.026995806
        else:
            if input[3] < 1.9914001:
                if input[2] < 1.9741608:
                    if input[5] < -0.84108895:
                        var20 = -0.025926176
                    else:
                        if input[1] < 1.1594853:
                            var20 = 0.06838713
                        else:
                            var20 = -0.005893197
                else:
                    var20 = -0.045116074
            else:
                if input[1] < 0.79870826:
                    var20 = -0.0125099365
                else:
                    var20 = -0.07586489
    if input[1] < 0.39784485:
        var21 = -0.090364546
    else:
        if input[4] < -0.6193539:
            var21 = 0.09308747
        else:
            if input[4] < 0.6924515:
                if input[6] < -0.48139668:
                    if input[1] < 0.8788809:
                        if input[6] < -0.90327317:
                            var21 = 0.033920746
                        else:
                            var21 = 0.13012074
                    else:
                        if input[2] < 0.9532552:
                            var21 = 0.034581825
                        else:
                            var21 = -0.037525807
                else:
                    if input[5] < -0.5347561:
                        var21 = -0.07101041
                    else:
                        var21 = 0.023651166
            else:
                if input[2] < 1.9741608:
                    if input[3] < 0.8355525:
                        var21 = 0.024718566
                    else:
                        var21 = -0.03352795
                else:
                    var21 = -0.06689439
    if input[1] < 0.39784485:
        var22 = -0.08903261
    else:
        if input[4] < 0.036548793:
            if input[6] < -0.65014726:
                if input[1] < 1.3198307:
                    var22 = 0.09488573
                else:
                    var22 = 0.0255957
            else:
                if input[6] < -0.41389644:
                    var22 = 0.0031515118
                else:
                    var22 = 0.021000141
        else:
            if input[3] < 1.9914001:
                if input[2] < 1.9741608:
                    if input[6] < -0.9370233:
                        var22 = 0.07600618
                    else:
                        if input[5] < 0.020472169:
                            var22 = 0.03646752
                        else:
                            var22 = -0.077033326
                else:
                    var22 = -0.04126857
            else:
                if input[1] < 0.79870826:
                    var22 = -0.012563835
                else:
                    var22 = -0.073976874
    if input[1] < 0.39784485:
        var23 = -0.087683074
    else:
        if input[4] < -0.6193539:
            var23 = 0.08933564
        else:
            if input[1] < 1.3198307:
                if input[3] < 1.9914001:
                    if input[6] < -0.9370233:
                        if input[4] < 0.6924515:
                            var23 = 0.097560875
                        else:
                            var23 = 0.01831269
                    else:
                        if input[5] < 0.020472169:
                            var23 = 0.038142998
                        else:
                            var23 = -0.08034122
                else:
                    if input[6] < -0.70077246:
                        var23 = -0.0074631483
                    else:
                        var23 = -0.06978934
            else:
                if input[2] < -0.06765037:
                    var23 = 0.017241208
                else:
                    var23 = -0.08453869
    if input[6] < 0.12610549:
        if input[4] < -0.6193539:
            var24 = 0.08716997
        else:
            if input[1] < 1.3198307:
                if input[3] < 1.9914001:
                    if input[6] < -0.9370233:
                        if input[4] < 0.6924515:
                            var24 = 0.09398736
                        else:
                            var24 = 0.017354062
                    else:
                        if input[5] < 0.020472169:
                            var24 = 0.034932047
                        else:
                            var24 = -0.080770865
                else:
                    if input[2] < -1.0885559:
                        var24 = -0.0020467767
                    else:
                        var24 = -0.05084535
            else:
                if input[2] < -0.06765037:
                    var24 = 0.016314583
                else:
                    var24 = -0.08154931
    else:
        var24 = -0.08654015
    if input[6] < -0.19452065:
        if input[4] < 0.036548793:
            if input[6] < -0.65014726:
                if input[1] < 1.3198307:
                    var25 = 0.08892414
                else:
                    var25 = 0.023264248
            else:
                var25 = 0.007213596
        else:
            if input[1] < 0.79870826:
                if input[5] < -0.20289554:
                    var25 = 0.09550187
                else:
                    var25 = -0.010366301
            else:
                if input[3] < 1.9914001:
                    if input[6] < -0.9370233:
                        if input[0] < 1.0:
                            var25 = -0.0120340595
                        else:
                            var25 = 0.066604294
                    else:
                        if input[6] < -0.565772:
                            var25 = -0.08373039
                        else:
                            var25 = 0.022590118
                else:
                    var25 = -0.06991731
    else:
        if input[4] < 0.36450014:
            var25 = 0.010498754
        else:
            var25 = -0.08753243
    if input[1] < 0.39784485:
        var26 = -0.083763085
    else:
        if input[4] < -0.6193539:
            var26 = 0.08378514
        else:
            if input[1] < 1.3198307:
                if input[3] < 1.9914001:
                    if input[6] < -0.9370233:
                        if input[4] < 0.6924515:
                            var26 = 0.088812344
                        else:
                            var26 = 0.015046152
                    else:
                        if input[5] < 0.020472169:
                            var26 = 0.031963576
                        else:
                            var26 = -0.07406748
                else:
                    if input[6] < -0.70077246:
                        var26 = -0.0050120004
                    else:
                        var26 = -0.065455504
            else:
                if input[2] < -0.06765037:
                    var26 = 0.015509901
                else:
                    var26 = -0.07885925
    if input[1] < 0.39784485:
        var27 = -0.08232262
    else:
        if input[4] < -0.6193539:
            var27 = 0.081765674
        else:
            if input[4] < 0.6924515:
                if input[1] < 0.79870826:
                    var27 = 0.06633238
                else:
                    if input[2] < 0.9532552:
                        if input[5] < 0.10981925:
                            var27 = 0.038946047
                        else:
                            var27 = -0.02503078
                    else:
                        if input[5] < 0.12896505:
                            var27 = -0.06690302
                        else:
                            var27 = 0.03132784
            else:
                if input[2] < 1.9741608:
                    if input[3] < 0.8355525:
                        var27 = 0.02245949
                    else:
                        var27 = -0.028461484
                else:
                    var27 = -0.0633046
    if input[6] < -0.295771:
        if input[4] < 0.036548793:
            if input[1] < 1.3198307:
                var28 = 0.078518905
            else:
                var28 = 0.011366493
        else:
            if input[1] < 0.79870826:
                if input[5] < -0.20289554:
                    var28 = 0.092986435
                else:
                    var28 = -0.00786379
            else:
                if input[6] < -0.9370233:
                    if input[3] < 0.8355525:
                        if input[5] < 0.9905262:
                            var28 = 0.001133967
                        else:
                            var28 = 0.05735687
                    else:
                        var28 = -0.046513736
                else:
                    if input[6] < -0.565772:
                        var28 = -0.08354099
                    else:
                        var28 = 0.012695165
    else:
        if input[4] < 0.36450014:
            var28 = 0.013562219
        else:
            var28 = -0.0857827
    if input[6] < -0.19452065:
        if input[4] < 0.036548793:
            if input[6] < -0.65014726:
                if input[2] < 0.9532552:
                    var29 = 0.0849713
                else:
                    var29 = 0.019827906
            else:
                var29 = 0.00040828637
        else:
            if input[1] < 0.79870826:
                if input[5] < -0.20289554:
                    var29 = 0.081944965
                else:
                    var29 = -0.008534289
            else:
                if input[3] < 1.9914001:
                    if input[6] < -0.9370233:
                        if input[0] < 1.0:
                            var29 = -0.01340766
                        else:
                            var29 = 0.060205467
                    else:
                        if input[6] < -0.565772:
                            var29 = -0.07776906
                        else:
                            var29 = 0.019992001
                else:
                    var29 = -0.0654596
    else:
        if input[4] < 0.36450014:
            var29 = 0.006840471
        else:
            var29 = -0.08253866
    if input[1] < 0.39784485:
        var30 = -0.07816338
    else:
        if input[4] < -0.6193539:
            var30 = 0.07728956
        else:
            if input[1] < 1.3198307:
                if input[3] < 1.9914001:
                    if input[6] < -0.9370233:
                        if input[4] < 0.6924515:
                            var30 = 0.08301013
                        else:
                            var30 = 0.012875429
                    else:
                        if input[5] < 0.020472169:
                            var30 = 0.028542748
                        else:
                            var30 = -0.06979144
                else:
                    if input[1] < 0.8788809:
                        var30 = -0.01072749
                    else:
                        var30 = -0.049989395
            else:
                if input[2] < -0.06765037:
                    var30 = 0.012372146
                else:
                    var30 = -0.07438585
    if input[6] < -0.295771:
        if input[4] < 0.036548793:
            if input[1] < 1.3198307:
                var31 = 0.073049076
            else:
                var31 = 0.007823403
        else:
            if input[1] < 0.79870826:
                if input[5] < -0.20289554:
                    var31 = 0.08179086
                else:
                    var31 = -0.0062960642
            else:
                if input[3] < 1.9914001:
                    if input[6] < -0.9370233:
                        if input[0] < 1.0:
                            var31 = -0.013953008
                        else:
                            var31 = 0.055369355
                    else:
                        if input[6] < -0.565772:
                            var31 = -0.07518873
                        else:
                            var31 = 0.016522568
                else:
                    var31 = -0.062353164
    else:
        if input[1] < 0.8788809:
            var31 = -0.07806908
        else:
            var31 = 0.0207564
    if input[1] < 0.39784485:
        var32 = -0.07521897
    else:
        if input[4] < -0.6193539:
            var32 = 0.07443138
        else:
            if input[1] < 1.3198307:
                if input[3] < 1.9914001:
                    if input[6] < -0.295771:
                        if input[4] < 0.6924515:
                            var32 = 0.056507852
                        else:
                            var32 = -0.0034778886
                    else:
                        var32 = -0.029089509
                else:
                    if input[1] < 0.8788809:
                        var32 = -0.009891402
                    else:
                        var32 = -0.047880378
            else:
                if input[2] < -0.06765037:
                    var32 = 0.01217711
                else:
                    var32 = -0.0718153
    if input[6] < 0.12610549:
        if input[4] < -0.6193539:
            var33 = 0.07258383
        else:
            if input[1] < 1.3198307:
                if input[3] < 1.9914001:
                    if input[6] < -0.9370233:
                        if input[4] < 0.6924515:
                            var33 = 0.077247
                        else:
                            var33 = 0.011277603
                    else:
                        if input[5] < 0.020472169:
                            var33 = 0.024388975
                        else:
                            var33 = -0.07033483
                else:
                    if input[1] < 0.9590536:
                        var33 = -0.007851246
                    else:
                        var33 = -0.040680032
            else:
                var33 = -0.037770703
    else:
        var33 = -0.07389994
    if input[6] < -0.295771:
        if input[4] < 0.036548793:
            if input[2] < 0.9532552:
                var34 = 0.07059448
            else:
                var34 = 0.006276697
        else:
            if input[1] < 0.75862193:
                var34 = 0.05932032
            else:
                if input[3] < 1.9914001:
                    if input[0] < 1.0:
                        if input[6] < -0.565772:
                            var34 = -0.041271847
                        else:
                            var34 = 0.025462953
                    else:
                        var34 = 0.025049632
                else:
                    var34 = -0.066062085
    else:
        if input[4] < 0.36450014:
            var34 = 0.012136574
        else:
            var34 = -0.078984514
    if input[1] < 0.39784485:
        var35 = -0.07085945
    else:
        if input[4] < -0.6193539:
            var35 = 0.06962083
        else:
            if input[1] < 1.3198307:
                if input[3] < 1.9914001:
                    if input[6] < -0.9370233:
                        if input[4] < 0.6924515:
                            var35 = 0.07468394
                        else:
                            var35 = 0.009655238
                    else:
                        if input[5] < 0.020472169:
                            var35 = 0.022514988
                        else:
                            var35 = -0.06587381
                else:
                    if input[1] < 0.8788809:
                        var35 = -0.0068909205
                    else:
                        var35 = -0.044125635
            else:
                var35 = -0.036363654
    if input[6] < -0.295771:
        if input[4] < 0.036548793:
            if input[2] < 0.9532552:
                var36 = 0.067498736
            else:
                var36 = 0.0046237567
        else:
            if input[1] < 0.79870826:
                if input[5] < -0.20289554:
                    var36 = 0.07383468
                else:
                    var36 = -0.00639712
            else:
                if input[6] < -0.9370233:
                    if input[3] < 0.8355525:
                        var36 = 0.027629709
                    else:
                        var36 = -0.039969016
                else:
                    if input[6] < -0.565772:
                        var36 = -0.07512687
                    else:
                        var36 = 0.0068818503
    else:
        if input[4] < 0.36450014:
            var36 = 0.010423384
        else:
            var36 = -0.07660413
    if input[1] < 0.39784485:
        var37 = -0.06787032
    else:
        if input[4] < -0.6193539:
            var37 = 0.066783205
        else:
            if input[1] < 1.3198307:
                if input[3] < 1.9914001:
                    if input[6] < -0.9370233:
                        if input[4] < 0.6924515:
                            var37 = 0.071902744
                        else:
                            var37 = 0.008372803
                    else:
                        if input[5] < 0.020472169:
                            var37 = 0.020894803
                        else:
                            var37 = -0.063208476
                else:
                    if input[1] < 0.8788809:
                        var37 = -0.006200375
                    else:
                        var37 = -0.04284812
            else:
                var37 = -0.035447072
    if input[6] < -0.295771:
        if input[4] < 0.036548793:
            if input[2] < 0.9532552:
                var38 = 0.0645648
            else:
                var38 = 0.0032009538
        else:
            if input[1] < 0.75862193:
                var38 = 0.055762775
            else:
                if input[3] < 1.9914001:
                    if input[0] < 1.0:
                        if input[6] < -0.565772:
                            var38 = -0.039625492
                        else:
                            var38 = 0.022399515
                    else:
                        var38 = 0.021010503
                else:
                    var38 = -0.061398376
    else:
        if input[1] < 0.8788809:
            var38 = -0.0705543
        else:
            var38 = 0.01722764
    if input[6] < -0.295771:
        if input[4] < 0.036548793:
            if input[2] < 0.9532552:
                var39 = 0.06187733
            else:
                var39 = 0.0030080702
        else:
            if input[1] < 0.79870826:
                if input[4] < 0.6924515:
                    var39 = 0.06896278
                else:
                    var39 = -0.008950896
            else:
                if input[6] < -0.9370233:
                    if input[5] < 0.014090234:
                        var39 = -0.035670705
                    else:
                        var39 = 0.025450801
                else:
                    if input[6] < -0.565772:
                        var39 = -0.07161759
                    else:
                        var39 = 0.0054830774
    else:
        if input[4] < 0.36450014:
            var39 = 0.010096661
        else:
            var39 = -0.07290712
    if input[4] < -0.6193539:
        var40 = 0.06335364
    else:
        if input[6] < -0.295771:
            if input[1] < 0.75862193:
                var40 = 0.05282804
            else:
                if input[4] < 0.036548793:
                    if input[2] < 0.9532552:
                        var40 = 0.044188883
                    else:
                        var40 = -0.018429108
                else:
                    if input[3] < 1.9914001:
                        if input[2] < 0.9532552:
                            var40 = 0.015637266
                        else:
                            var40 = -0.019638313
                    else:
                        var40 = -0.059529062
        else:
            if input[1] < 0.8387946:
                var40 = -0.074475855
            else:
                var40 = 0.0015188314
    if input[4] < -0.6193539:
        var41 = 0.061717667
    else:
        if input[6] < -0.295771:
            if input[1] < 0.79870826:
                if input[6] < -0.81889784:
                    var41 = -0.018782545
                else:
                    var41 = 0.073755376
            else:
                if input[2] < 0.9532552:
                    if input[5] < -0.79641545:
                        var41 = 0.051469125
                    else:
                        if input[6] < -0.85264796:
                            var41 = 0.016766934
                        else:
                            var41 = -0.05410443
                else:
                    if input[5] < 0.3587147:
                        var41 = -0.06898487
                    else:
                        var41 = 0.025781138
        else:
            if input[1] < 0.8387946:
                var41 = -0.072734825
            else:
                var41 = 0.0014402206
    if input[1] < 0.39784485:
        var42 = -0.06075409
    else:
        if input[4] < -0.6193539:
            var42 = 0.060119696
        else:
            if input[1] < 1.3198307:
                if input[2] < -1.0885559:
                    var42 = -0.03966398
                else:
                    if input[3] < 1.9914001:
                        if input[4] < 0.6924515:
                            var42 = 0.046841223
                        else:
                            var42 = -0.010426159
                    else:
                        var42 = -0.039090928
            else:
                var42 = -0.03496438
    if input[4] < -0.6193539:
        var43 = 0.05856023
    else:
        if input[6] < -0.295771:
            if input[1] < 0.75862193:
                var43 = 0.048073314
            else:
                if input[4] < 0.036548793:
                    if input[2] < 0.9532552:
                        var43 = 0.042564813
                    else:
                        var43 = -0.015069469
                else:
                    if input[3] < 1.9914001:
                        if input[0] < 1.0:
                            var43 = -0.017654125
                        else:
                            var43 = 0.01766074
                    else:
                        var43 = -0.056991667
        else:
            if input[1] < 0.8387946:
                var43 = -0.07000763
            else:
                var43 = -0.00014660334
    if input[4] < -0.6193539:
        var44 = 0.057039745
    else:
        if input[6] < -0.295771:
            if input[1] < 0.79870826:
                if input[6] < -0.81889784:
                    var44 = -0.018197471
                else:
                    var44 = 0.06845995
            else:
                if input[2] < 0.9532552:
                    if input[5] < -0.79641545:
                        var44 = 0.048357327
                    else:
                        if input[6] < -0.85264796:
                            var44 = 0.016792694
                        else:
                            var44 = -0.05199626
                else:
                    if input[5] < 0.3587147:
                        var44 = -0.06552898
                    else:
                        var44 = 0.023159688
        else:
            if input[1] < 0.8387946:
                var44 = -0.06829799
            else:
                var44 = -0.00013902162
    var45 = var0 + var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8 + var9 + var10 + var11 + var12 + var13 + var14 + var15 + var16 + var17 + var18 + var19 + var20 + var21 + var22 + var23 + var24 + var25 + var26 + var27 + var28 + var29 + var30 + var31 + var32 + var33 + var34 + var35 + var36 + var37 + var38 + var39 + var40 + var41 + var42 + var43 + var44
    if input[4] < 0.36450014:
        if input[5] < -0.61772126:
            if input[6] < -0.4307715:
                var46 = 0.01886636
            else:
                var46 = -0.052015692
        else:
            if input[5] < 0.116201185:
                var46 = 0.06501796
            else:
                var46 = 0.011448951
    else:
        if input[6] < -0.295771:
            if input[6] < -0.7176475:
                if input[0] < 1.0:
                    var46 = -0.051001012
                else:
                    var46 = 0.0069337348
            else:
                if input[5] < -0.51561034:
                    var46 = 0.06753088
                else:
                    var46 = -0.0091529265
        else:
            var46 = -0.06556084
    if input[4] < -0.6193539:
        var47 = 0.054934323
    else:
        if input[6] < -0.295771:
            if input[1] < 0.79870826:
                if input[6] < -0.81889784:
                    var47 = -0.016903244
                else:
                    var47 = 0.06491508
            else:
                if input[2] < 0.9532552:
                    if input[5] < -0.79641545:
                        var47 = 0.0448114
                    else:
                        if input[6] < -0.85264796:
                            var47 = 0.014658782
                        else:
                            var47 = -0.050539352
                else:
                    if input[5] < 0.3587147:
                        var47 = -0.062455524
                    else:
                        var47 = 0.021833723
        else:
            if input[1] < 0.8387946:
                var47 = -0.06521158
            else:
                var47 = 0.00015853571
    if input[4] < 0.36450014:
        if input[5] < -0.61772126:
            if input[6] < -0.4307715:
                var48 = 0.017462244
            else:
                var48 = -0.04925462
        else:
            if input[1] < 1.1594853:
                var48 = 0.061974477
            else:
                var48 = 0.008339865
    else:
        if input[6] < -0.295771:
            if input[6] < -0.7176475:
                if input[0] < 1.0:
                    var48 = -0.04892567
                else:
                    var48 = 0.0058774687
            else:
                if input[5] < -0.51561034:
                    var48 = 0.06307169
                else:
                    var48 = -0.009168541
        else:
            var48 = -0.062785916
    if input[4] < -0.6193539:
        var49 = 0.052817285
    else:
        if input[6] < -0.295771:
            if input[1] < 0.79870826:
                if input[6] < -0.81889784:
                    var49 = -0.016161108
                else:
                    var49 = 0.061651237
            else:
                if input[4] < 0.036548793:
                    if input[2] < 0.9532552:
                        var49 = 0.03778895
                    else:
                        var49 = -0.016412226
                else:
                    if input[6] < -0.9370233:
                        if input[6] < -1.4264001:
                            var49 = -0.029211173
                        else:
                            var49 = 0.024527993
                    else:
                        if input[6] < -0.565772:
                            var49 = -0.06537642
                        else:
                            var49 = 0.004346395
        else:
            if input[1] < 0.8387946:
                var49 = -0.062341046
            else:
                var49 = 0.00039240843
    if input[4] < 0.36450014:
        if input[5] < -0.61772126:
            if input[6] < -0.5151468:
                var50 = 0.013769825
            else:
                var50 = -0.045377303
        else:
            if input[5] < 0.116201185:
                var50 = 0.06023827
            else:
                var50 = 0.008701993
    else:
        if input[6] < -0.295771:
            if input[6] < -0.7176475:
                if input[0] < 1.0:
                    var50 = -0.046004694
                else:
                    var50 = 0.00576367
            else:
                if input[5] < -0.51561034:
                    var50 = 0.060103264
                else:
                    var50 = -0.00991409
        else:
            var50 = -0.060098242
    if input[4] < 0.36450014:
        if input[5] < -0.61772126:
            if input[4] < -0.29140255:
                var51 = 0.014019231
            else:
                var51 = -0.035723083
        else:
            if input[1] < 1.1594853:
                var51 = 0.057453163
            else:
                var51 = 0.0054767113
    else:
        if input[5] < -0.834707:
            if input[1] < 0.8788809:
                var51 = 0.038356554
            else:
                var51 = -0.010817773
        else:
            if input[0] < 1.0:
                var51 = -0.059681833
            else:
                if input[7] < -0.6233225:
                    var51 = -0.03232762
                else:
                    var51 = 0.03122049
    if input[4] < 0.36450014:
        if input[5] < -0.61772126:
            if input[4] < -0.29140255:
                var52 = 0.013327924
            else:
                var52 = -0.03373469
        else:
            if input[5] < 0.116201185:
                var52 = 0.056004103
            else:
                var52 = 0.0057730065
    else:
        if input[6] < -0.295771:
            if input[6] < -0.565772:
                if input[1] < 0.79870826:
                    var52 = 0.0134483995
                else:
                    if input[0] < 1.0:
                        var52 = -0.06754485
                    else:
                        var52 = 0.018239168
            else:
                var52 = 0.03794701
        else:
            var52 = -0.058167435
    if input[6] < -0.295771:
        if input[1] < 0.75862193:
            var53 = 0.042093515
        else:
            if input[4] < 0.036548793:
                if input[2] < 0.9532552:
                    var53 = 0.04516891
                else:
                    var53 = -0.0056660995
            else:
                if input[3] < 1.9914001:
                    if input[5] < -0.7772696:
                        var53 = 0.017410953
                    else:
                        if input[6] < -1.139524:
                            var53 = 0.013253236
                        else:
                            var53 = -0.04811708
                else:
                    var53 = -0.056633025
    else:
        if input[4] < 0.36450014:
            var53 = 0.007660204
        else:
            var53 = -0.05668936
    if input[6] < -0.41389644:
        if input[5] < -0.7772696:
            if input[6] < -0.7176475:
                var54 = 0.0018080885
            else:
                var54 = 0.071589775
        else:
            if input[6] < -0.85264796:
                if input[4] < 0.036548793:
                    var54 = 0.045606073
                else:
                    if input[5] < 0.3587147:
                        var54 = -0.026066644
                    else:
                        var54 = 0.006257233
            else:
                var54 = -0.063134246
    else:
        if input[5] < -0.4773187:
            var54 = -0.058701713
        else:
            if input[1] < 0.75862193:
                var54 = 0.001998388
            else:
                var54 = 0.012502359
    if input[4] < 0.36450014:
        if input[5] < -0.61772126:
            if input[4] < -0.29140255:
                var55 = 0.012703291
            else:
                var55 = -0.032887492
        else:
            if input[1] < 1.1594853:
                var55 = 0.052734938
            else:
                var55 = 0.002235623
    else:
        if input[5] < -0.834707:
            if input[5] < -1.1027483:
                var55 = 0.02216239
            else:
                var55 = 0.002859781
        else:
            if input[0] < 1.0:
                var55 = -0.055258047
            else:
                if input[7] < -0.6233225:
                    var55 = -0.030727535
                else:
                    var55 = 0.030327106
    if input[6] < -0.295771:
        if input[1] < 0.79870826:
            if input[6] < -0.81889784:
                var56 = -0.011884216
            else:
                var56 = 0.05875647
        else:
            if input[4] < 0.036548793:
                if input[2] < 0.9532552:
                    var56 = 0.042476248
                else:
                    var56 = -0.01161874
            else:
                if input[6] < -0.9370233:
                    if input[6] < -1.3926499:
                        var56 = -0.024838567
                    else:
                        var56 = 0.027810443
                else:
                    if input[6] < -0.565772:
                        var56 = -0.059807565
                    else:
                        var56 = 0.0033124543
    else:
        if input[4] < 0.36450014:
            var56 = 0.0066457675
        else:
            var56 = -0.054130286
    if input[6] < -0.41389644:
        if input[5] < -0.7772696:
            if input[6] < -0.7176475:
                var57 = 0.002005316
            else:
                var57 = 0.067808926
        else:
            if input[6] < -0.85264796:
                if input[4] < 0.036548793:
                    var57 = 0.04236552
                else:
                    if input[5] < 0.3587147:
                        var57 = -0.023470648
                    else:
                        var57 = 0.0062491475
            else:
                var57 = -0.06030755
    else:
        if input[5] < -0.4773187:
            var57 = -0.05595327
        else:
            var57 = 0.00911664
    if input[6] < -0.41389644:
        if input[5] < -0.7772696:
            if input[6] < -0.7176475:
                var58 = 0.001880809
            else:
                var58 = 0.06533396
        else:
            if input[6] < -0.85264796:
                if input[4] < 0.036548793:
                    var58 = 0.040570267
                else:
                    if input[5] < 0.3587147:
                        var58 = -0.02237465
                    else:
                        var58 = 0.0058419104
            else:
                var58 = -0.057973344
    else:
        if input[3] < 0.8355525:
            var58 = -0.049521804
        else:
            var58 = 0.014031543
    if input[4] < 0.36450014:
        if input[5] < -0.61772126:
            if input[4] < -0.29140255:
                var59 = 0.012217157
            else:
                var59 = -0.03188544
        else:
            if input[5] < 0.116201185:
                var59 = 0.05156466
            else:
                var59 = 0.0013738562
    else:
        if input[6] < -0.295771:
            if input[6] < -0.81889784:
                if input[0] < 1.0:
                    var59 = -0.05528999
                else:
                    var59 = 0.008415407
            else:
                if input[1] < 0.79870826:
                    var59 = 0.053551115
                else:
                    var59 = -0.009623061
        else:
            var59 = -0.05126627
    if input[6] < -0.41389644:
        if input[5] < -0.7772696:
            if input[6] < -0.7176475:
                var60 = 0.0023819136
            else:
                var60 = 0.062983416
        else:
            if input[6] < -0.85264796:
                if input[4] < 0.036548793:
                    var60 = 0.037901603
                else:
                    if input[5] < 0.3587147:
                        var60 = -0.021121819
                    else:
                        var60 = 0.0051590106
            else:
                var60 = -0.055552423
    else:
        if input[5] < -0.4773187:
            var60 = -0.052057542
        else:
            var60 = 0.00869007
    if input[4] < 0.36450014:
        if input[5] < -0.61772126:
            if input[5] < -0.936818:
                var61 = 0.0071776765
            else:
                var61 = -0.026010474
        else:
            if input[0] < 1.0:
                var61 = 0.048468485
            else:
                var61 = -0.00139521
    else:
        if input[5] < -0.834707:
            var61 = 0.013805366
        else:
            if input[6] < -0.9370233:
                var61 = 0.0015821931
            else:
                if input[5] < -0.011437503:
                    var61 = -0.013043195
                else:
                    var61 = -0.057412535
    if input[6] < -0.41389644:
        if input[5] < -0.7772696:
            if input[6] < -0.7176475:
                var62 = 0.0016496055
            else:
                var62 = 0.060488027
        else:
            if input[6] < -0.85264796:
                if input[4] < 0.036548793:
                    var62 = 0.035587993
                else:
                    if input[5] < 0.3587147:
                        var62 = -0.020545183
                    else:
                        var62 = 0.005034206
            else:
                var62 = -0.053025592
    else:
        if input[5] < -0.4773187:
            var62 = -0.04956017
        else:
            var62 = 0.00847689
    if input[4] < 0.36450014:
        if input[3] < -0.32029513:
            var63 = -0.02205016
        else:
            if input[2] < -1.0885559:
                var63 = -0.015043246
            else:
                if input[6] < -1.0551487:
                    var63 = 0.0038823106
                else:
                    var63 = 0.052128006
    else:
        if input[5] < -0.834707:
            var63 = 0.011861123
        else:
            if input[0] < 1.0:
                var63 = -0.049092792
            else:
                if input[6] < -1.1057739:
                    var63 = 0.02300799
                else:
                    var63 = -0.026429242
    if input[6] < -0.295771:
        if input[1] < 1.3198307:
            if input[3] < 1.9914001:
                if input[7] < -0.6233225:
                    var64 = -0.006757244
                else:
                    if input[5] < -0.8666167:
                        var64 = -0.00087101426
                    else:
                        var64 = 0.057167064
            else:
                var64 = -0.02539291
        else:
            var64 = -0.028070232
    else:
        var64 = -0.025784913
    if input[4] < 0.36450014:
        if input[3] < -0.32029513:
            var65 = -0.021261817
        else:
            if input[2] < -1.0885559:
                var65 = -0.012828653
            else:
                if input[6] < -1.0551487:
                    var65 = 0.0035496503
                else:
                    var65 = 0.049762897
    else:
        if input[5] < -0.834707:
            var65 = 0.010906409
        else:
            if input[0] < 1.0:
                var65 = -0.047664978
            else:
                if input[5] < 0.69695723:
                    var65 = 0.02402292
                else:
                    var65 = -0.024380287
    if input[6] < -1.1057739:
        if input[6] < -1.3926499:
            if input[3] < 0.8355525:
                var66 = -0.013234799
            else:
                var66 = 0.006631434
        else:
            var66 = 0.035322264
    else:
        if input[5] < 0.020472169:
            if input[1] < 0.8387946:
                if input[5] < -0.7708877:
                    var66 = 0.03639777
                else:
                    var66 = -0.0068535875
            else:
                if input[2] < 0.9532552:
                    if input[5] < -0.79641545:
                        var66 = 0.02929301
                    else:
                        var66 = 0.00020160917
                else:
                    var66 = -0.0489583
        else:
            var66 = -0.038741186
    if input[4] < 0.36450014:
        if input[5] < -0.61772126:
            if input[5] < -0.936818:
                var67 = 0.0066482
            else:
                var67 = -0.025640124
        else:
            if input[5] < 0.116201185:
                var67 = 0.046465736
            else:
                var67 = -0.00021912825
    else:
        if input[5] < -0.834707:
            var67 = 0.00937248
        else:
            if input[0] < 1.0:
                var67 = -0.045308586
            else:
                if input[5] < 0.69695723:
                    var67 = 0.023214642
                else:
                    var67 = -0.02342025
    if input[6] < -0.295771:
        if input[1] < 1.3198307:
            if input[3] < 1.9914001:
                if input[7] < -0.6233225:
                    var68 = -0.004198731
                else:
                    if input[5] < -0.8666167:
                        var68 = -0.0020667564
                    else:
                        var68 = 0.054671954
            else:
                var68 = -0.024367532
        else:
            var68 = -0.026072264
    else:
        var68 = -0.025103157
    if input[4] < 0.36450014:
        if input[5] < -0.61772126:
            if input[5] < -0.936818:
                var69 = 0.007055835
            else:
                var69 = -0.024637949
        else:
            if input[1] < 1.1594853:
                var69 = 0.04428443
            else:
                var69 = -0.0031488098
    else:
        if input[5] < -0.834707:
            var69 = 0.008646728
        else:
            if input[6] < -0.9370233:
                var69 = 0.0014527334
            else:
                var69 = -0.04061285
    if input[4] < 0.036548793:
        if input[6] < -0.65014726:
            var70 = 0.03537032
        else:
            var70 = -0.01703876
    else:
        if input[3] < 1.9914001:
            if input[5] < -0.8666167:
                var70 = -0.030790588
            else:
                if input[5] < 0.10981925:
                    if input[3] < 0.8355525:
                        var70 = 0.009568168
                    else:
                        var70 = 0.046086825
                else:
                    if input[6] < -1.1057739:
                        var70 = 0.025084605
                    else:
                        var70 = -0.047916073
        else:
            var70 = -0.03912565
    if input[1] < 1.3198307:
        if input[6] < -0.41389644:
            if input[3] < 1.9914001:
                if input[4] < 0.6924515:
                    var71 = 0.047617894
                else:
                    var71 = -0.010898296
            else:
                var71 = -0.017130515
        else:
            if input[5] < -0.4773187:
                var71 = -0.04558824
            else:
                var71 = 0.010756242
    else:
        var71 = -0.025983786
    if input[4] < 0.036548793:
        if input[6] < -0.65014726:
            var72 = 0.033652224
        else:
            var72 = -0.015211693
    else:
        if input[3] < 1.9914001:
            if input[5] < -0.8666167:
                var72 = -0.029928619
            else:
                if input[5] < 0.10981925:
                    if input[3] < 0.8355525:
                        var72 = 0.008525179
                    else:
                        var72 = 0.043970633
                else:
                    if input[6] < -1.1057739:
                        var72 = 0.02358212
                    else:
                        var72 = -0.047117468
        else:
            var72 = -0.036886174
    if input[1] < 1.3198307:
        if input[6] < -0.41389644:
            if input[5] < -0.6623948:
                var73 = 0.041152336
            else:
                if input[6] < -0.9370233:
                    if input[6] < -1.3926499:
                        var73 = 0.0021255198
                    else:
                        var73 = 0.037331883
                else:
                    var73 = -0.04479732
        else:
            if input[3] < 0.8355525:
                var73 = -0.040263496
            else:
                var73 = 0.0131216915
    else:
        var73 = -0.025777733
    if input[4] < 0.036548793:
        if input[6] < -0.65014726:
            var74 = 0.0323366
        else:
            var74 = -0.0132044405
    else:
        if input[3] < 1.9914001:
            if input[5] < -0.8666167:
                var74 = -0.029210417
            else:
                if input[5] < 0.10981925:
                    var74 = 0.030400878
                else:
                    if input[6] < -1.139524:
                        var74 = 0.012492148
                    else:
                        var74 = -0.03177483
        else:
            var74 = -0.036041148
    if input[1] < 1.3198307:
        if input[6] < -0.41389644:
            if input[5] < -0.6623948:
                var75 = 0.039190926
            else:
                if input[6] < -0.9370233:
                    if input[6] < -1.3926499:
                        var75 = 0.0014907748
                    else:
                        var75 = 0.035618335
                else:
                    var75 = -0.04259173
        else:
            if input[5] < -0.4773187:
                var75 = -0.041829146
            else:
                var75 = 0.010503369
    else:
        var75 = -0.025591617
    if input[4] < 0.036548793:
        if input[6] < -0.65014726:
            var76 = 0.03113217
        else:
            var76 = -0.011186637
    else:
        if input[3] < 1.9914001:
            if input[3] < 0.8355525:
                if input[6] < -0.9370233:
                    var76 = 0.01951233
                else:
                    if input[5] < -0.7772696:
                        var76 = -0.0052381544
                    else:
                        var76 = -0.054112136
            else:
                var76 = 0.021809481
        else:
            var76 = -0.035093058
    if input[1] < 1.3198307:
        if input[1] < 0.91896725:
            if input[6] < -0.295771:
                if input[4] < 0.6924515:
                    var77 = 0.03096014
                else:
                    var77 = -0.023306541
            else:
                var77 = -0.04515684
        else:
            if input[5] < -0.6241032:
                var77 = -0.006571947
            else:
                if input[1] < 1.119399:
                    var77 = 0.040360905
                else:
                    var77 = 0.010426978
    else:
        var77 = -0.025474671
    if input[4] < 0.036548793:
        if input[2] < 0.9532552:
            var78 = 0.030012352
        else:
            var78 = -0.010340857
    else:
        if input[3] < 1.9914001:
            if input[5] < -0.8666167:
                var78 = -0.029158393
            else:
                if input[5] < 0.10981925:
                    var78 = 0.028686265
                else:
                    if input[1] < 0.8788809:
                        var78 = -0.02437688
                    else:
                        var78 = 0.0029294027
        else:
            var78 = -0.034146093
    if input[4] < 0.036548793:
        if input[6] < -0.65014726:
            var79 = 0.029529858
        else:
            var79 = -0.011089346
    else:
        if input[3] < 1.9914001:
            if input[3] < 0.8355525:
                if input[6] < -0.9370233:
                    var79 = 0.018052585
                else:
                    if input[5] < -0.834707:
                        var79 = -0.008881937
                    else:
                        var79 = -0.046747874
            else:
                var79 = 0.01998068
        else:
            var79 = -0.032756913
    if input[1] < 1.3198307:
        if input[4] < -0.29140255:
            var80 = 0.030692954
        else:
            if input[3] < 1.9914001:
                if input[6] < -0.9370233:
                    var80 = 0.032712337
                else:
                    if input[3] < 0.8355525:
                        if input[5] < -0.7772696:
                            var80 = -0.0047233095
                        else:
                            var80 = -0.04428269
                    else:
                        var80 = 0.024056515
            else:
                var80 = -0.032685384
    else:
        var80 = -0.025792984
    if input[2] < 1.9741608:
        if input[5] < -1.0261651:
            var81 = 0.033643384
        else:
            if input[5] < -0.5985755:
                var81 = -0.035916287
            else:
                if input[1] < 1.1594853:
                    if input[6] < -1.1057739:
                        var81 = 0.046211343
                    else:
                        if input[2] < -0.06765037:
                            var81 = 0.013172992
                        else:
                            var81 = -0.016628137
                else:
                    var81 = -0.01215695
    else:
        var81 = -0.024016077
    if input[4] < 0.036548793:
        if input[2] < 0.9532552:
            var82 = 0.028364927
        else:
            var82 = -0.010443503
    else:
        if input[7] < 0.019086907:
            if input[6] < -0.9370233:
                var82 = 0.001995914
            else:
                var82 = -0.042612262
        else:
            if input[1] < 0.79870826:
                var82 = 0.02777472
            else:
                var82 = -0.018111706
    if input[1] < 1.3198307:
        if input[1] < 0.91896725:
            if input[6] < -0.295771:
                if input[1] < 0.75862193:
                    var83 = 0.038368262
                else:
                    var83 = -0.0135923205
            else:
                var83 = -0.042953365
        else:
            if input[5] < -0.6241032:
                var83 = -0.005184335
            else:
                if input[1] < 1.119399:
                    var83 = 0.03769426
                else:
                    var83 = 0.010087148
    else:
        var83 = -0.024341602
    if input[4] < 0.036548793:
        if input[6] < -0.65014726:
            var84 = 0.028751388
        else:
            var84 = -0.010482381
    else:
        if input[5] < -0.20289554:
            if input[5] < -0.8666167:
                var84 = -0.019392312
            else:
                var84 = 0.025413264
        else:
            if input[1] < 0.91896725:
                var84 = -0.034571275
            else:
                var84 = 0.00018515487
    if input[1] < 1.3198307:
        if input[2] < -1.0885559:
            var85 = -0.022867449
        else:
            if input[4] < 0.036548793:
                var85 = 0.05409658
            else:
                if input[5] < -0.8666167:
                    var85 = -0.027515972
                else:
                    if input[5] < -0.47093678:
                        var85 = 0.03629529
                    else:
                        if input[1] < 0.91896725:
                            var85 = -0.023513755
                        else:
                            var85 = 0.010068861
    else:
        var85 = -0.024161307
    if input[2] < 1.9741608:
        if input[5] < -1.0261651:
            var86 = 0.033613827
        else:
            if input[5] < -0.5985755:
                var86 = -0.034101903
            else:
                if input[1] < 1.1594853:
                    if input[6] < -0.9370233:
                        var86 = 0.040185425
                    else:
                        var86 = -0.0010842428
                else:
                    var86 = -0.011580386
    else:
        var86 = -0.022946455
    if input[5] < -0.7772696:
        if input[2] < 0.9532552:
            var87 = 0.034066055
        else:
            var87 = -0.016586458
    else:
        if input[1] < 0.91896725:
            if input[1] < 0.75862193:
                var87 = 0.0060154623
            else:
                var87 = -0.045410674
        else:
            if input[1] < 1.119399:
                var87 = 0.035074275
            else:
                if input[4] < 0.036548793:
                    var87 = 0.001215658
                else:
                    var87 = -0.024325695
    if input[1] < 1.3198307:
        if input[6] < -0.41389644:
            if input[5] < -0.6623948:
                var88 = 0.037512377
            else:
                if input[6] < -0.9370233:
                    if input[6] < -1.3926499:
                        var88 = -0.0014045461
                    else:
                        var88 = 0.030233303
                else:
                    var88 = -0.038303915
        else:
            if input[5] < -0.4773187:
                var88 = -0.037898876
            else:
                var88 = 0.012920531
    else:
        var88 = -0.022589086
    if input[4] < 0.036548793:
        if input[2] < 0.9532552:
            var89 = 0.028614802
        else:
            var89 = -0.010297422
    else:
        if input[7] < -0.6233225:
            var89 = -0.02709571
        else:
            if input[1] < 0.79870826:
                var89 = 0.020072408
            else:
                if input[6] < -0.565772:
                    var89 = -0.036975402
                else:
                    var89 = 0.018024558
    if input[4] < 0.036548793:
        if input[6] < -0.65014726:
            var90 = 0.027359113
        else:
            var90 = -0.010163437
    else:
        if input[7] < -0.6233225:
            var90 = -0.025613917
        else:
            if input[1] < 0.79870826:
                var90 = 0.018779015
            else:
                if input[6] < -0.565772:
                    var90 = -0.035095524
                else:
                    var90 = 0.01705916
    if input[1] < 1.3198307:
        if input[6] < -0.41389644:
            if input[3] < 1.9914001:
                if input[4] < 0.6924515:
                    var91 = 0.042087514
                else:
                    var91 = -0.010422928
            else:
                var91 = -0.014705868
        else:
            if input[5] < -0.4773187:
                var91 = -0.03748834
            else:
                var91 = 0.011059668
    else:
        var91 = -0.021988641
    if input[4] < 0.036548793:
        if input[6] < -0.65014726:
            var92 = 0.026165342
        else:
            var92 = -0.008913905
    else:
        if input[7] < -0.6233225:
            var92 = -0.024665581
        else:
            if input[1] < 0.79870826:
                var92 = 0.017503975
            else:
                if input[6] < -0.565772:
                    var92 = -0.034230586
                else:
                    var92 = 0.016145475
    if input[1] < 1.3198307:
        if input[6] < -0.41389644:
            if input[5] < -0.6623948:
                var93 = 0.03447258
            else:
                if input[6] < -0.9370233:
                    if input[6] < -1.3926499:
                        var93 = 0.001047743
                    else:
                        var93 = 0.029996559
                else:
                    var93 = -0.036183845
        else:
            if input[5] < -0.4773187:
                var93 = -0.03614658
            else:
                var93 = 0.009996752
    else:
        var93 = -0.021434827
    if input[4] < 0.036548793:
        if input[6] < -0.7513976:
            var94 = 0.025050828
        else:
            var94 = -0.0069046556
    else:
        if input[7] < -0.6233225:
            var94 = -0.023834867
        else:
            if input[5] < -0.8666167:
                var94 = -0.020114081
            else:
                if input[5] < -0.47093678:
                    var94 = 0.028635377
                else:
                    var94 = -0.0060739443
    if input[2] < 1.9741608:
        if input[6] < -1.1057739:
            if input[1] < 1.1594853:
                var95 = 0.03872501
            else:
                var95 = -0.00032293308
        else:
            if input[3] < 0.8355525:
                if input[4] < 0.36450014:
                    var95 = 0.0016717475
                else:
                    var95 = -0.032645237
            else:
                if input[6] < -0.5488969:
                    var95 = -0.013092227
                else:
                    var95 = 0.020186847
    else:
        var95 = -0.021629913
    if input[4] < -0.29140255:
        var96 = 0.017062413
    else:
        if input[2] < 1.9741608:
            if input[6] < -1.1057739:
                var96 = 0.025356611
            else:
                if input[3] < 0.8355525:
                    var96 = -0.02707157
                else:
                    if input[6] < -0.48139668:
                        var96 = -0.0013414958
                    else:
                        var96 = 0.009409616
        else:
            var96 = -0.032589033
    if input[1] < 1.3198307:
        if input[6] < -0.41389644:
            if input[3] < 1.9914001:
                if input[4] < 0.6924515:
                    var97 = 0.03999424
                else:
                    var97 = -0.008300013
            else:
                var97 = -0.01428854
        else:
            if input[3] < 0.8355525:
                var97 = -0.029907474
            else:
                var97 = 0.0084405355
    else:
        var97 = -0.021393672
    if input[4] < 0.036548793:
        if input[5] < -0.61772126:
            var98 = -0.0053119273
        else:
            var98 = 0.025868187
    else:
        if input[1] < 0.75862193:
            var98 = 0.00921443
        else:
            if input[1] < 0.91896725:
                var98 = -0.028599128
            else:
                if input[1] < 1.119399:
                    var98 = 0.02180777
                else:
                    var98 = -0.0210641
    if input[1] < 1.3198307:
        if input[6] < -0.41389644:
            if input[3] < 1.9914001:
                if input[4] < 0.6924515:
                    var99 = 0.038347654
                else:
                    var99 = -0.0078741405
            else:
                var99 = -0.0134575395
        else:
            if input[3] < 0.8355525:
                var99 = -0.028795857
            else:
                var99 = 0.007948699
    else:
        var99 = -0.020561187
    if input[4] < 0.036548793:
        if input[5] < -0.61772126:
            var100 = -0.00467449
        else:
            var100 = 0.02507782
    else:
        if input[1] < 0.75862193:
            var100 = 0.009099775
        else:
            if input[5] < -0.47093678:
                var100 = 0.0022363386
            else:
                if input[1] < 0.9590536:
                    var100 = -0.03512457
                else:
                    var100 = -0.0055168434
    var101 = sigmoid(var45 + var46 + var47 + var48 + var49 + var50 + var51 + var52 + var53 + var54 + var55 + var56 + var57 + var58 + var59 + var60 + var61 + var62 + var63 + var64 + var65 + var66 + var67 + var68 + var69 + var70 + var71 + var72 + var73 + var74 + var75 + var76 + var77 + var78 + var79 + var80 + var81 + var82 + var83 + var84 + var85 + var86 + var87 + var88 + var89 + var90 + var91 + var92 + var93 + var94 + var95 + var96 + var97 + var98 + var99 + var100)
    return [1.0 - var101, var101]
