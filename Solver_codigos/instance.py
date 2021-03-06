class Shift:
	'''
	prohibitNext = {shiftId}
	'''
	def __init__(self):
		self.id = ''
		self.length = 0
		self.prohibitNext = set()

class ShiftRequest:
	def __init__(self):
		self.id = ''
		self.day = 0
		self.weight = 0

class StaffMember:
	'''
	maxShifts = {shiftID: maxCount}, ommited shifts are unconstrained
	shiftOnRequests = {day: ShiftRequest}
	shiftOffRequests = {day: ShiftRequest}
	maxWeekends = Maximum working weekends allowed
	'''
	def __init__(self):
		self.id = ''
		self.maxShifts = dict()
		self.maxTotalMinutes = 0
		self.minTotalMinutes = 0
		self.maxConsecutiveShifts = 0
		self.minConsecutiveShifts = 0
		self.minConsecutiveDaysOff = 0
		self.maxWeekends = 0
		self.Costo = 0 #aqui
		self.Contratado = False
		self.CostoExtra50 = 0 #aqui
		self.CostoExtra100 = 0 #aqui
		self.CostoExtra200 = 0 #aqui
		self.CostoExtraExterno = 0 #aqui
		self.daysOff = set()
		self.shiftOnRequests = dict()
		self.shiftOffRequests = dict()

class Costos:
		#Costos
    def __init__(self):
        self.daysOffWeight = 0
        self.prohibitNextWeight = 0
        self.maxShiftsWeight = 0 
        self.minTotalMinutesWeight = 0 #aqui
        self.maxTotalMinutesWeight = 0 #aqui
        self.minConsecutiveShiftsWeight = 0 #aqui
        self.maxConsecutiveShiftsWeight = 0 #aqui
        self.minConsecutiveDaysOffWeight = 0 #aqui
        self.weekendsWeight = 0 #aqui
        self.externalWeight = 0 #aqui
#        self.requirementUnderWeight = 0 #aqui
#        self.requirementOverWeight = 0 #aqui

class Cover:
	def __init__(self):
		self.day = 0
		self.shiftId = ''
		self.requirement =  0
		self.weightForUnder = 0
		self.weightForOver = 0

class ProblemInstance:
	'''
	Every problem starts on a Monday at index 0

	shifts = {shiftId: Shift}
	staff = {staffId: StaffMember}
	cover = [{shiftId: Cover}], index = dayIndex
	'''
	def __init__(self):
		self.horizon = 0
		self.HorasPorSemana = 0
		self.maxExtraHours = 0
		self.shifts = dict()
		self.staff = dict()
		self.cover = list()
		self.costos = Costos()
		self.hardConstraintWeight = 0
		self.ContratadosObligados = False
		self.feriados = list()