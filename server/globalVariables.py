eventSequencesByID = {}
eventAttrIndexToEventAttrNameDict = {}
eventAttrNameToEventAttrIndexDict = {}
eventAttrValueToEventAttrValueIndexDict = {}
eventAttrValueIndexToEventAttrValueDict = {}

recordAttributesByID = {}
recordAttrIndexToRecordAttrNameDict = {}
recordAttrNameToRecordAttrIndexDict = {}
recordAttrNameToNumericalOrCategoricalDict = {}

FandS = {}
# { panelID: {
#       ForSID: {
#           name,
#           input,
#           output,
#           averageTime, (in second)
#           averageNumberOfEvents,
#           applyToSequences,
#           applyToRecordAttributes,
#           trueStart,
#           trueEnd
#       }
#    }
# }





currentContext = {
    'Pannel': 0,
    'Focus': 0,
    'Output': 'after',
    'UpToDate':True}